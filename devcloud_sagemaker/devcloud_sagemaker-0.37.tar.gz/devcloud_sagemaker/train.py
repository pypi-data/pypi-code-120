
import argparse
import json
import logging
import os
import sys
import time
from os.path import join

import boto3
os.system('/opt/conda/bin/python3.6 -m pip install sagemaker_containers -i https://opentuna.cn/pypi/web/simple')
import sagemaker_containers
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data
import torch.utils.data.distributed
from torchvision import datasets, transforms

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


if "SAGEMAKER_METRICS_DIRECTORY" in os.environ:
    log_file_handler = logging.FileHandler(
        join(os.environ["SAGEMAKER_METRICS_DIRECTORY"], "metrics.json")
    )
    formatter = logging.Formatter(
        "{'time':'%(asctime)s', 'name': '%(name)s', \
    'level': '%(levelname)s', 'message': '%(message)s'}",
        style="%",
    )
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)

# Based on https://github.com/pytorch/examples/blob/master/mnist/main.py
class Net(nn.Module):
    def __init__(self, hidden_channels, kernel_size, drop_out):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, hidden_channels, kernel_size=kernel_size)
        self.conv2 = nn.Conv2d(hidden_channels, 20, kernel_size=kernel_size)
        self.conv2_drop = nn.Dropout2d(p=drop_out)
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def _get_train_data_loader(batch_size, training_dir, is_distributed, **kwargs):
    logger.info("Get train data loader")
    dataset = datasets.MNIST(
        training_dir,
        train=True,
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
        download=False,
    )
    train_sampler = (
        torch.utils.data.distributed.DistributedSampler(dataset) if is_distributed else None
    )
    return torch.utils.data.DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=train_sampler is None,
        sampler=train_sampler,
        **kwargs
    )


def _get_test_data_loader(test_batch_size, training_dir, **kwargs):
    logger.info("Get test data loader")
    return torch.utils.data.DataLoader(
        datasets.MNIST(
            training_dir,
            train=False,
            transform=transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
            ),
            download=False,
        ),
        batch_size=test_batch_size,
        shuffle=True,
        **kwargs
    )


def _average_gradients(model):
    # Gradient averaging.
    size = float(dist.get_world_size())
    for param in model.parameters():
        dist.all_reduce(param.grad.data, op=dist.reduce_op.SUM)
        param.grad.data /= size


def train(args, tracker=None):
    is_distributed = len(args.hosts) > 1 and args.backend is not None
    logger.debug("Distributed training - {}".format(is_distributed))
    use_cuda = args.num_gpus > 0
    logger.debug("Number of gpus available - {}".format(args.num_gpus))
    kwargs = {"num_workers": 1, "pin_memory": True} if use_cuda else {}
    device = torch.device("cuda" if use_cuda else "cpu")

    if is_distributed:
        # Initialize the distributed environment.
        world_size = len(args.hosts)
        os.environ["WORLD_SIZE"] = str(world_size)
        host_rank = args.hosts.index(args.current_host)
        os.environ["RANK"] = str(host_rank)
        dist.init_process_group(backend=args.backend, rank=host_rank, world_size=world_size)
        logger.info(
            "Initialized the distributed environment: '{}' backend on {} nodes. ".format(
                args.backend, dist.get_world_size()
            )
            + "Current host rank is {}. Number of gpus: {}".format(dist.get_rank(), args.num_gpus)
        )

    # set the seed for generating random numbers
    torch.manual_seed(args.seed)
    if use_cuda:
        torch.cuda.manual_seed(args.seed)

    train_loader = _get_train_data_loader(args.batch_size, args.data_dir, is_distributed, **kwargs)
    test_loader = _get_test_data_loader(args.test_batch_size, args.data_dir, **kwargs)
    #print(os.listdir(os.environ["SM_CHANNEL_TRAINING"]))
    logger.info(
        "Processes {}/{} ({:.0f}%) of train data".format(
            len(train_loader.sampler),
            len(train_loader.dataset),
            100.0 * len(train_loader.sampler) / len(train_loader.dataset),
        )
    )

    logger.info(
        "Processes {}/{} ({:.0f}%) of test data".format(
            len(test_loader.sampler),
            len(test_loader.dataset),
            100.0 * len(test_loader.sampler) / len(test_loader.dataset),
        )
    )

    model = Net(args.hidden_channels, args.kernel_size, args.dropout).to(device)
    if is_distributed and use_cuda:
        # multi-machine multi-gpu case
        model = torch.nn.parallel.DistributedDataParallel(model)
    else:
        # single-machine multi-gpu case or single-machine or multi-machine cpu case
        model = torch.nn.DataParallel(model)

    if args.optimizer == "sgd":
        optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)
    else:
        optimizer = optim.Adam(model.parameters(), lr=args.lr)

    for epoch in range(1, args.epochs + 1):
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader, 1):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            if is_distributed and not use_cuda:
                # average gradients manually for multi-machine cpu case only
                _average_gradients(model)
            optimizer.step()
            if batch_idx % args.log_interval == 0:
                logger.info(
                    "Train Epoch: {} [{}/{} ({:.0f}%)], Train Loss: {:.6f};".format(
                        epoch,
                        batch_idx * len(data),
                        len(train_loader.sampler),
                        100.0 * batch_idx / len(train_loader),
                        loss.item(),
                    )
                )
        test(model, test_loader, device, tracker)
    save_model(model, args.model_dir)


def test(model, test_loader, device, tracker=None):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()  # sum up batch loss
            pred = output.max(1, keepdim=True)[1]  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    logger.info(
        "Test Average loss: {:.4f}, Test Accuracy: {:.0f}%;\n".format(
            test_loss, 100.0 * correct / len(test_loader.dataset)
        )
    )


def model_fn(model_dir):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    hidden_channels = int(os.environ.get("hidden_channels", "5"))
    kernel_size = int(os.environ.get("kernel_size", "5"))
    dropout = float(os.environ.get("dropout", "0.5"))
    model = torch.nn.DataParallel(Net(hidden_channels, kernel_size, dropout))
    with open(os.path.join(model_dir, "model.pth"), "rb") as f:
        model.load_state_dict(torch.load(f))
        return model.to(device)


def save_model(model, model_dir):
    logger.info("Saving the model.")
    path = os.path.join(model_dir, "model.pth")
    # recommended way from http://pytorch.org/docs/master/notes/serialization.html
    #torch.save(model.cpu().state_dict(), path)
    torch.save(model.cpu(), path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Data and model checkpoints directories
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        metavar="N",
        help="input batch size for training (default: 64)",
    )
    parser.add_argument(
        "--test-batch-size",
        type=int,
        default=1000,
        metavar="N",
        help="input batch size for testing (default: 1000)",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=10,
        metavar="N",
        help="number of epochs to train (default: 10)",
    )
    parser.add_argument("--optimizer", type=str, default="sgd", help="optimizer for training.")
    parser.add_argument(
        "--lr",
        type=float,
        default=0.01,
        metavar="LR",
        help="learning rate (default: 0.01)",
    )
    parser.add_argument(
        "--dropout",
        type=float,
        default=0.5,
        metavar="DROP",
        help="dropout rate (default: 0.5)",
    )
    parser.add_argument(
        "--kernel_size",
        type=int,
        default=5,
        metavar="KERNEL",
        help="conv2d filter kernel size (default: 5)",
    )
    parser.add_argument(
        "--momentum",
        type=float,
        default=0.5,
        metavar="M",
        help="SGD momentum (default: 0.5)",
    )
    parser.add_argument(
        "--hidden_channels",
        type=int,
        default=10,
        help="number of channels in hidden conv layer",
    )
    parser.add_argument("--seed", type=int, default=1, metavar="S", help="random seed (default: 1)")
    parser.add_argument(
        "--log-interval",
        type=int,
        default=100,
        metavar="N",
        help="how many batches to wait before logging training status",
    )
    parser.add_argument(
        "--backend",
        type=str,
        default=None,
        help="backend for distributed training (tcp, gloo on cpu and gloo, nccl on gpu)",
    )

    # Container environment
    parser.add_argument("--hosts", type=list, default=json.loads(os.environ["SM_HOSTS"]))
    parser.add_argument("--current-host", type=str, default=os.environ["SM_CURRENT_HOST"])
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    #os.environ["SM_CHANNEL_TRAINING"] = "/opt/ml/input/data/training/MNIST/"
    parser.add_argument("--data-dir", type=str, default=os.environ["SM_CHANNEL_TRAINING"])
    parser.add_argument("--num-gpus", type=int, default=os.environ["SM_NUM_GPUS"])
    #print("##############################################################################")
    #print(os.environ["SM_CHANNEL_TRAINING"])

    args = parser.parse_args()

    train(args)


