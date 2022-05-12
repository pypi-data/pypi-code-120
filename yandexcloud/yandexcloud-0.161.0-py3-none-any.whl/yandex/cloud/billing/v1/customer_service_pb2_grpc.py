# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.billing.v1 import customer_service_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class CustomerServiceStub(object):
    """A set of methods for managing Customer resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.billing.v1.CustomerService/List',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersResponse.FromString,
                )
        self.Invite = channel.unary_unary(
                '/yandex.cloud.billing.v1.CustomerService/Invite',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.InviteCustomerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Activate = channel.unary_unary(
                '/yandex.cloud.billing.v1.CustomerService/Activate',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ActivateCustomerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Suspend = channel.unary_unary(
                '/yandex.cloud.billing.v1.CustomerService/Suspend',
                request_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.SuspendCustomerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class CustomerServiceServicer(object):
    """A set of methods for managing Customer resources.
    """

    def List(self, request, context):
        """Retrieves the list of customers associated with the specified reseller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Invite(self, request, context):
        """Invites customer to the specified reseller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Activate(self, request, context):
        """Activates specified customer. After customer is activated, he can use resources associated with his billing account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Suspend(self, request, context):
        """Suspend specified customer. After customer is suspended, he can't use resources associated with his billing account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersResponse.SerializeToString,
            ),
            'Invite': grpc.unary_unary_rpc_method_handler(
                    servicer.Invite,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.InviteCustomerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ActivateCustomerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Suspend': grpc.unary_unary_rpc_method_handler(
                    servicer.Suspend,
                    request_deserializer=yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.SuspendCustomerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.billing.v1.CustomerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerService(object):
    """A set of methods for managing Customer resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.CustomerService/List',
            yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersRequest.SerializeToString,
            yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ListCustomersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Invite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.CustomerService/Invite',
            yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.InviteCustomerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Activate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.CustomerService/Activate',
            yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.ActivateCustomerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Suspend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.billing.v1.CustomerService/Suspend',
            yandex_dot_cloud_dot_billing_dot_v1_dot_customer__service__pb2.SuspendCustomerRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
