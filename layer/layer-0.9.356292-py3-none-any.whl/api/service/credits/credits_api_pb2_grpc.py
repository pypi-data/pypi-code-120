# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layer.api.service.credits import credits_api_pb2 as api_dot_service_dot_credits_dot_credits__api__pb2


class CreditsAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCreditLogV2 = channel.unary_unary(
                '/api.CreditsAPI/GetCreditLogV2',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.FromString,
                )
        self.RecordBillableActivity = channel.unary_unary(
                '/api.CreditsAPI/RecordBillableActivity',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.FromString,
                )
        self.ChangeCreditBalance = channel.unary_unary(
                '/api.CreditsAPI/ChangeCreditBalance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceResponse.FromString,
                )
        self.GetMonthlyBillingReport = channel.unary_unary(
                '/api.CreditsAPI/GetMonthlyBillingReport',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.FromString,
                )
        self.GetDailyBillingReport = channel.unary_unary(
                '/api.CreditsAPI/GetDailyBillingReport',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportResponse.FromString,
                )
        self.GetCreditsBalance = channel.unary_unary(
                '/api.CreditsAPI/GetCreditsBalance',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.FromString,
                )
        self.GetWeeklyUsageReport = channel.unary_unary(
                '/api.CreditsAPI/GetWeeklyUsageReport',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.FromString,
                )
        self.CreateTier = channel.unary_unary(
                '/api.CreditsAPI/CreateTier',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierResponse.FromString,
                )
        self.GetFreeTierId = channel.unary_unary(
                '/api.CreditsAPI/GetFreeTierId',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdResponse.FromString,
                )
        self.GetTierById = channel.unary_unary(
                '/api.CreditsAPI/GetTierById',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdResponse.FromString,
                )
        self.UpdateTier = channel.unary_unary(
                '/api.CreditsAPI/UpdateTier',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierResponse.FromString,
                )
        self.GetTiers = channel.unary_unary(
                '/api.CreditsAPI/GetTiers',
                request_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersResponse.FromString,
                )


class CreditsAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCreditLogV2(self, request, context):
        """v2
        if we were using packages we could use package versions:
        https://github.com/uber/prototool/blob/dev/style/README.md#directory-structure
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordBillableActivity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeCreditBalance(self, request, context):
        """v1
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMonthlyBillingReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDailyBillingReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCreditsBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWeeklyUsageReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFreeTierId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTierById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTiers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreditsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCreditLogV2': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCreditLogV2,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.SerializeToString,
            ),
            'RecordBillableActivity': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordBillableActivity,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.SerializeToString,
            ),
            'ChangeCreditBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeCreditBalance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceResponse.SerializeToString,
            ),
            'GetMonthlyBillingReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMonthlyBillingReport,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.SerializeToString,
            ),
            'GetDailyBillingReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDailyBillingReport,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportResponse.SerializeToString,
            ),
            'GetCreditsBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCreditsBalance,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.SerializeToString,
            ),
            'GetWeeklyUsageReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeeklyUsageReport,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.SerializeToString,
            ),
            'CreateTier': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTier,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierResponse.SerializeToString,
            ),
            'GetFreeTierId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFreeTierId,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdResponse.SerializeToString,
            ),
            'GetTierById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTierById,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdResponse.SerializeToString,
            ),
            'UpdateTier': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTier,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierResponse.SerializeToString,
            ),
            'GetTiers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTiers,
                    request_deserializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersRequest.FromString,
                    response_serializer=api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.CreditsAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreditsAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCreditLogV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetCreditLogV2',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Request.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditLogV2Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordBillableActivity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/RecordBillableActivity',
            api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.RecordBillableActivityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeCreditBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/ChangeCreditBalance',
            api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.ChangeCreditBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMonthlyBillingReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetMonthlyBillingReport',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetMonthlyBillingReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDailyBillingReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetDailyBillingReport',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetDailyBillingReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCreditsBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetCreditsBalance',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetCreditsBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWeeklyUsageReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetWeeklyUsageReport',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetWeeklyUsageReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/CreateTier',
            api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.CreateTierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFreeTierId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetFreeTierId',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetFreeTierIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTierById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetTierById',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetTierByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/UpdateTier',
            api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.UpdateTierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTiers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.CreditsAPI/GetTiers',
            api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersRequest.SerializeToString,
            api_dot_service_dot_credits_dot_credits__api__pb2.GetTiersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
