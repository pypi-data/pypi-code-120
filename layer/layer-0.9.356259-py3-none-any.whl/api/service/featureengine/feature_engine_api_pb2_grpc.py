# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layer.api.service.featureengine import feature_engine_api_pb2 as api_dot_service_dot_featureengine_dot_feature__engine__api__pb2


class FeatureEngineAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartBuildDatasetByPath = channel.unary_unary(
                '/api.FeatureEngineAPI/StartBuildDatasetByPath',
                request_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathResponse.FromString,
                )
        self.GetBuildDatasetStatus = channel.unary_unary(
                '/api.FeatureEngineAPI/GetBuildDatasetStatus',
                request_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusResponse.FromString,
                )
        self.CancelBuildDataset = channel.unary_unary(
                '/api.FeatureEngineAPI/CancelBuildDataset',
                request_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetResponse.FromString,
                )


class FeatureEngineAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartBuildDatasetByPath(self, request, context):
        """Dataset Build
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBuildDatasetStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelBuildDataset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeatureEngineAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartBuildDatasetByPath': grpc.unary_unary_rpc_method_handler(
                    servicer.StartBuildDatasetByPath,
                    request_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathRequest.FromString,
                    response_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathResponse.SerializeToString,
            ),
            'GetBuildDatasetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBuildDatasetStatus,
                    request_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusRequest.FromString,
                    response_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusResponse.SerializeToString,
            ),
            'CancelBuildDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelBuildDataset,
                    request_deserializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetRequest.FromString,
                    response_serializer=api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.FeatureEngineAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FeatureEngineAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartBuildDatasetByPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FeatureEngineAPI/StartBuildDatasetByPath',
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathRequest.SerializeToString,
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.StartBuildDatasetByPathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBuildDatasetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FeatureEngineAPI/GetBuildDatasetStatus',
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusRequest.SerializeToString,
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.GetBuildDatasetStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelBuildDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FeatureEngineAPI/CancelBuildDataset',
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetRequest.SerializeToString,
            api_dot_service_dot_featureengine_dot_feature__engine__api__pb2.CancelBuildDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
