# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Keras layers API.
"""

import sys as _sys

from keras.api._v1.keras.layers import experimental
from keras.engine.base_layer import Layer
from keras.engine.base_layer_utils import disable_v2_dtype_behavior
from keras.engine.base_layer_utils import enable_v2_dtype_behavior
from keras.engine.input_layer import Input
from keras.engine.input_layer import InputLayer
from keras.engine.input_spec import InputSpec
from keras.feature_column.dense_features import DenseFeatures
from keras.layers.activation.elu import ELU
from keras.layers.activation.leaky_relu import LeakyReLU
from keras.layers.activation.prelu import PReLU
from keras.layers.activation.relu import ReLU
from keras.layers.activation.softmax import Softmax
from keras.layers.activation.thresholded_relu import ThresholdedReLU
from keras.layers.attention.additive_attention import AdditiveAttention
from keras.layers.attention.attention import Attention
from keras.layers.attention.multi_head_attention import MultiHeadAttention
from keras.layers.convolutional.conv1d import Conv1D
from keras.layers.convolutional.conv1d import Conv1D as Convolution1D
from keras.layers.convolutional.conv1d_transpose import Conv1DTranspose
from keras.layers.convolutional.conv1d_transpose import Conv1DTranspose as Convolution1DTranspose
from keras.layers.convolutional.conv2d import Conv2D
from keras.layers.convolutional.conv2d import Conv2D as Convolution2D
from keras.layers.convolutional.conv2d_transpose import Conv2DTranspose
from keras.layers.convolutional.conv2d_transpose import Conv2DTranspose as Convolution2DTranspose
from keras.layers.convolutional.conv3d import Conv3D
from keras.layers.convolutional.conv3d import Conv3D as Convolution3D
from keras.layers.convolutional.conv3d_transpose import Conv3DTranspose
from keras.layers.convolutional.conv3d_transpose import Conv3DTranspose as Convolution3DTranspose
from keras.layers.convolutional.depthwise_conv1d import DepthwiseConv1D
from keras.layers.convolutional.depthwise_conv2d import DepthwiseConv2D
from keras.layers.convolutional.separable_conv1d import SeparableConv1D
from keras.layers.convolutional.separable_conv1d import SeparableConv1D as SeparableConvolution1D
from keras.layers.convolutional.separable_conv2d import SeparableConv2D
from keras.layers.convolutional.separable_conv2d import SeparableConv2D as SeparableConvolution2D
from keras.layers.core.activation import Activation
from keras.layers.core.dense import Dense
from keras.layers.core.einsum_dense import EinsumDense
from keras.layers.core.embedding import Embedding
from keras.layers.core.lambda_layer import Lambda
from keras.layers.core.masking import Masking
from keras.layers.locally_connected.locally_connected1d import LocallyConnected1D
from keras.layers.locally_connected.locally_connected2d import LocallyConnected2D
from keras.layers.merging.add import Add
from keras.layers.merging.add import add
from keras.layers.merging.average import Average
from keras.layers.merging.average import average
from keras.layers.merging.concatenate import Concatenate
from keras.layers.merging.concatenate import concatenate
from keras.layers.merging.dot import Dot
from keras.layers.merging.dot import dot
from keras.layers.merging.maximum import Maximum
from keras.layers.merging.maximum import maximum
from keras.layers.merging.minimum import Minimum
from keras.layers.merging.minimum import minimum
from keras.layers.merging.multiply import Multiply
from keras.layers.merging.multiply import multiply
from keras.layers.merging.subtract import Subtract
from keras.layers.merging.subtract import subtract
from keras.layers.normalization.batch_normalization_v1 import BatchNormalization
from keras.layers.normalization.layer_normalization import LayerNormalization
from keras.layers.pooling.average_pooling1d import AveragePooling1D
from keras.layers.pooling.average_pooling1d import AveragePooling1D as AvgPool1D
from keras.layers.pooling.average_pooling2d import AveragePooling2D
from keras.layers.pooling.average_pooling2d import AveragePooling2D as AvgPool2D
from keras.layers.pooling.average_pooling3d import AveragePooling3D
from keras.layers.pooling.average_pooling3d import AveragePooling3D as AvgPool3D
from keras.layers.pooling.global_average_pooling1d import GlobalAveragePooling1D
from keras.layers.pooling.global_average_pooling1d import GlobalAveragePooling1D as GlobalAvgPool1D
from keras.layers.pooling.global_average_pooling2d import GlobalAveragePooling2D
from keras.layers.pooling.global_average_pooling2d import GlobalAveragePooling2D as GlobalAvgPool2D
from keras.layers.pooling.global_average_pooling3d import GlobalAveragePooling3D
from keras.layers.pooling.global_average_pooling3d import GlobalAveragePooling3D as GlobalAvgPool3D
from keras.layers.pooling.global_max_pooling1d import GlobalMaxPooling1D
from keras.layers.pooling.global_max_pooling1d import GlobalMaxPooling1D as GlobalMaxPool1D
from keras.layers.pooling.global_max_pooling2d import GlobalMaxPooling2D
from keras.layers.pooling.global_max_pooling2d import GlobalMaxPooling2D as GlobalMaxPool2D
from keras.layers.pooling.global_max_pooling3d import GlobalMaxPooling3D
from keras.layers.pooling.global_max_pooling3d import GlobalMaxPooling3D as GlobalMaxPool3D
from keras.layers.pooling.max_pooling1d import MaxPooling1D
from keras.layers.pooling.max_pooling1d import MaxPooling1D as MaxPool1D
from keras.layers.pooling.max_pooling2d import MaxPooling2D
from keras.layers.pooling.max_pooling2d import MaxPooling2D as MaxPool2D
from keras.layers.pooling.max_pooling3d import MaxPooling3D
from keras.layers.pooling.max_pooling3d import MaxPooling3D as MaxPool3D
from keras.layers.preprocessing.category_encoding import CategoryEncoding
from keras.layers.preprocessing.discretization import Discretization
from keras.layers.preprocessing.hashing import Hashing
from keras.layers.preprocessing.image_preprocessing import CenterCrop
from keras.layers.preprocessing.image_preprocessing import Rescaling
from keras.layers.preprocessing.image_preprocessing import Resizing
from keras.layers.preprocessing.normalization import Normalization
from keras.layers.regularization.activity_regularization import ActivityRegularization
from keras.layers.regularization.alpha_dropout import AlphaDropout
from keras.layers.regularization.dropout import Dropout
from keras.layers.regularization.gaussian_dropout import GaussianDropout
from keras.layers.regularization.gaussian_noise import GaussianNoise
from keras.layers.regularization.spatial_dropout1d import SpatialDropout1D
from keras.layers.regularization.spatial_dropout2d import SpatialDropout2D
from keras.layers.regularization.spatial_dropout3d import SpatialDropout3D
from keras.layers.reshaping.cropping1d import Cropping1D
from keras.layers.reshaping.cropping2d import Cropping2D
from keras.layers.reshaping.cropping3d import Cropping3D
from keras.layers.reshaping.flatten import Flatten
from keras.layers.reshaping.permute import Permute
from keras.layers.reshaping.repeat_vector import RepeatVector
from keras.layers.reshaping.reshape import Reshape
from keras.layers.reshaping.up_sampling1d import UpSampling1D
from keras.layers.reshaping.up_sampling2d import UpSampling2D
from keras.layers.reshaping.up_sampling3d import UpSampling3D
from keras.layers.reshaping.zero_padding1d import ZeroPadding1D
from keras.layers.reshaping.zero_padding2d import ZeroPadding2D
from keras.layers.reshaping.zero_padding3d import ZeroPadding3D
from keras.layers.rnn.abstract_rnn_cell import AbstractRNNCell
from keras.layers.rnn.base_rnn import RNN
from keras.layers.rnn.base_wrapper import Wrapper
from keras.layers.rnn.bidirectional import Bidirectional
from keras.layers.rnn.conv_lstm1d import ConvLSTM1D
from keras.layers.rnn.conv_lstm2d import ConvLSTM2D
from keras.layers.rnn.conv_lstm3d import ConvLSTM3D
from keras.layers.rnn.cudnn_gru import CuDNNGRU
from keras.layers.rnn.cudnn_lstm import CuDNNLSTM
from keras.layers.rnn.gru_v1 import GRU
from keras.layers.rnn.gru_v1 import GRUCell
from keras.layers.rnn.lstm_v1 import LSTM
from keras.layers.rnn.lstm_v1 import LSTMCell
from keras.layers.rnn.simple_rnn import SimpleRNN
from keras.layers.rnn.simple_rnn import SimpleRNNCell
from keras.layers.rnn.stacked_rnn_cells import StackedRNNCells
from keras.layers.rnn.time_distributed import TimeDistributed
from keras.layers.serialization import deserialize
from keras.layers.serialization import serialize
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.layers", public_apis=None, deprecation=True,
      has_lite=False)
