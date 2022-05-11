"""Implementation of mcli get runs"""
from __future__ import annotations

import argparse
import datetime as dt
from dataclasses import dataclass
from typing import Any, Dict, Generator, List, Optional

from mcli.api.model.run_model import RunStatus
from mcli.cli.m_get.display import MCLIDisplayItem, MCLIGetDisplay, OutputDisplay
from mcli.config import MCLIConfig, MCLIConfigError
from mcli.serverside.platforms.instance_type import GPUType
from mcli.utils.utils_kube import KubeContext, group_pods_by_job, list_pods_across_contexts
from mcli.utils.utils_kube_labels import extract_label_values, label
from mcli.utils.utils_logging import FAIL, console, err_console


@dataclass
class RunDisplayItem(MCLIDisplayItem):
    """Tuple that extracts run data for display purposes.
    """
    platform: str
    gpu_type: GPUType
    gpu_num: int
    created_time: str
    status: RunStatus

    # Sweeps are deprecated for now
    # sweep: str

    @classmethod
    def from_pod_group(cls, pod_group: List[Dict[str, Any]]) -> RunDisplayItem:
        # There will always be at least one pod associated with a job
        pod = pod_group[0]
        pod_labels: Dict[str, Any] = dict(pod['metadata'].get('labels', {}))
        labels_to_get = [
            label.mosaic.JOB, label.compute.LABEL_MCLI_PLATFORM, label.compute.LABEL_GPU_TYPE,
            label.compute.LABEL_GPU_NUM
        ]
        label_vals = extract_label_values(pod_labels, labels_to_get, default='-')

        extracted: Dict[str, Any] = {'name': label_vals[label.mosaic.JOB]}
        extracted['platform'] = label_vals[label.compute.LABEL_MCLI_PLATFORM]
        extracted['gpu_type'] = label_vals[label.compute.LABEL_GPU_TYPE]
        extracted['gpu_num'] = label_vals[label.compute.LABEL_GPU_NUM]

        # Sweeps are deprecated for now
        # extracted['sweep'] = labels.get(label.mosaic.LABEL_SWEEP, '-')

        timezone = dt.datetime.now(dt.timezone.utc).astimezone().tzinfo
        iso_date = dt.datetime.fromisoformat(pod['metadata']['creationTimestamp']).astimezone(timezone)
        str_date = iso_date.strftime('%Y-%m-%d %I:%M %p')
        extracted['created_time'] = str_date

        status = pod.get('status', {}).get('phase', '')
        run_status = RunStatus.UNKNOWN
        if status == 'Pending':
            run_status = RunStatus.QUEUED
        elif status == 'Running':
            run_status = RunStatus.RUNNING
        elif status == 'Succeeded':
            run_status = RunStatus.SUCCEEDED
        elif status == 'Failed':
            run_status = RunStatus.FAILED
        extracted['status'] = run_status

        return cls(**extracted)


class MCLIRunDisplay(MCLIGetDisplay):

    def __init__(self, pod_grouping_by_job: Dict[str, Any]):
        self.grouping = pod_grouping_by_job

        # Each inner list is a group of pods associated with a job
        self.ordered_pod_groups: List[List[Dict[str,
                                                Any]]] = (sorted(self.grouping.values(),
                                                                 key=lambda x: x[0]['metadata']['creationTimestamp'],
                                                                 reverse=True))

    def __iter__(self) -> Generator[RunDisplayItem, None, None]:
        for pod_group in self.ordered_pod_groups:
            yield RunDisplayItem.from_pod_group(pod_group)


def get_runs(run_list: Optional[List[str]] = None,
             platform: Optional[str] = None,
             gpu_type: Optional[str] = None,
             gpu_num: Optional[str] = None,
             status: Optional[RunStatus] = None,
             output: OutputDisplay = OutputDisplay.TABLE,
             sort_by: str = 'updated_time',
             **kwargs) -> int:
    """Get a table of ongoing and completed runs
    """
    del status
    del kwargs
    del sort_by

    try:
        conf = MCLIConfig.load_config()
    except MCLIConfigError:
        err_console.print(f'{FAIL} MCLI not yet initialized. You must have at least one platform before you can get '
                          'runs. Please run `mcli init` and then `mcli create platform` to create your first platform.')
        return 1

    if not conf.platforms:
        err_console.print(f'{FAIL} No platforms created. You must have at least one platform before you can get '
                          'runs. Please run `mcli create platform` to create your first platform.')
        return 1

    if run_list is not None:
        raise NotImplementedError

    # Filter platforms
    if platform is not None:
        chosen_platforms = [p for p in conf.platforms if p.name == platform]
        if not chosen_platforms:
            platform_names = [p.name for p in conf.platforms]
            err_console.print(f'{FAIL} Platform not found. Platform name should be one of {platform_names}, '
                              f'not "{platform}".')
            return 1
    else:
        chosen_platforms = conf.platforms

    labels = {}
    # Filter instances
    if gpu_type is not None:
        labels[label.mosaic.compute_selectors.LABEL_GPU_TYPE] = gpu_type

    if gpu_num is not None:
        labels[label.mosaic.compute_selectors.LABEL_GPU_NUM] = gpu_num

    with console.status('Retrieving requested runs...'):
        contexts = [KubeContext(cluster=p.kubernetes_context, namespace=p.namespace, user='') for p in chosen_platforms]

        # Query for requested jobs
        all_pods, _ = list_pods_across_contexts(contexts=contexts, labels=labels)
        pod_grouping_by_job = group_pods_by_job(all_pods)

    display = MCLIRunDisplay(pod_grouping_by_job)
    display.print(output)

    return 0


def get_runs_argparser(subparsers):
    """Configures the ``mcli get runs`` argparser
    """
    # mcli get runs
    run_examples: str = """Examples:
    $ mcli get runs

    NAME                         PLATFORM   GPU_TYPE      GPU_NUM      CREATED_TIME     STATUS
    run-foo                      p-1        g0-type       8            05/06/22 1:58pm  succeeded
    run-bar                      p-2        g0-type       1            05/06/22 1:57pm  succeeded
    """
    runs_parser = subparsers.add_parser('runs',
                                        aliases=['run'],
                                        help='Get information on all of your existing runs across all platforms.',
                                        epilog=run_examples,
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    runs_parser.add_argument('--platform', help='Filter to just runs on a specific platform')
    runs_parser.add_argument('--gpu-type')
    runs_parser.add_argument('--gpu-num')
    runs_parser.set_defaults(func=get_runs)

    return runs_parser
