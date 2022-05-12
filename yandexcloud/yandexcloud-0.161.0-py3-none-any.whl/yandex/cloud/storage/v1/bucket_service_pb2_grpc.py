# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.storage.v1 import bucket_pb2 as yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2
from yandex.cloud.storage.v1 import bucket_service_pb2 as yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2


class BucketServiceStub(object):
    """A set of methods for managing buckets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/List',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/Get',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.Bucket.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/Create',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.CreateBucketRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/Update',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.UpdateBucketRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/Delete',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetStats = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/GetStats',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketStatsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.BucketStats.FromString,
                )
        self.GetHTTPSConfig = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/GetHTTPSConfig',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketHTTPSConfigRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.HTTPSConfig.FromString,
                )
        self.SetHTTPSConfig = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/SetHTTPSConfig',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.SetBucketHTTPSConfigRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteHTTPSConfig = channel.unary_unary(
                '/yandex.cloud.storage.v1.BucketService/DeleteHTTPSConfig',
                request_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketHTTPSConfigRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class BucketServiceServicer(object):
    """A set of methods for managing buckets.
    """

    def List(self, request, context):
        """Retrieves the list of buckets in the specified folder.

        The following fields will not be returned for buckets in the list: [Bucket.policy], [Bucket.acl], [Bucket.cors],
        [Bucket.website_settings], [Bucket.lifecycle_rules].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified bucket.

        To get the list of all available buckets, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a bucket in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified bucket.

        In most cases, `storage.editor` role (see [documentation](/docs/storage/security/#storage-editor)) should be enough
        to update a bucket, subject to its [policy](/docs/storage/concepts/policy).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStats(self, request, context):
        """Returns the statistics for the specified bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHTTPSConfig(self, request, context):
        """Returns the HTTPS configuration for the specified bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetHTTPSConfig(self, request, context):
        """Updates the HTTPS configuration for the specified bucket.

        The updated configuration could take up to 30 minutes to apply to the bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHTTPSConfig(self, request, context):
        """Deletes the HTTPS configuration for the specified bucket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BucketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.Bucket.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.CreateBucketRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.UpdateBucketRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStats,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketStatsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.BucketStats.SerializeToString,
            ),
            'GetHTTPSConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHTTPSConfig,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketHTTPSConfigRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.HTTPSConfig.SerializeToString,
            ),
            'SetHTTPSConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHTTPSConfig,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.SetBucketHTTPSConfigRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteHTTPSConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteHTTPSConfig,
                    request_deserializer=yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketHTTPSConfigRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.storage.v1.BucketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BucketService(object):
    """A set of methods for managing buckets.
    """

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/List',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsRequest.SerializeToString,
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.ListBucketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/Get',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketRequest.SerializeToString,
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.Bucket.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/Create',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.CreateBucketRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/Update',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.UpdateBucketRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/Delete',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/GetStats',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketStatsRequest.SerializeToString,
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.BucketStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHTTPSConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/GetHTTPSConfig',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.GetBucketHTTPSConfigRequest.SerializeToString,
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__pb2.HTTPSConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetHTTPSConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/SetHTTPSConfig',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.SetBucketHTTPSConfigRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteHTTPSConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.storage.v1.BucketService/DeleteHTTPSConfig',
            yandex_dot_cloud_dot_storage_dot_v1_dot_bucket__service__pb2.DeleteBucketHTTPSConfigRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
