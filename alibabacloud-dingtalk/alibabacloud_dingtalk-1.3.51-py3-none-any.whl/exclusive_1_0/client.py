# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        if UtilClient.empty(self._endpoint):
            self._endpoint = 'api.dingtalk.com'

    def add_org(
        self,
        request: dingtalkexclusive__1__0_models.AddOrgRequest,
    ) -> dingtalkexclusive__1__0_models.AddOrgResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.AddOrgHeaders()
        return self.add_org_with_options(request, headers, runtime)

    async def add_org_async(
        self,
        request: dingtalkexclusive__1__0_models.AddOrgRequest,
    ) -> dingtalkexclusive__1__0_models.AddOrgResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.AddOrgHeaders()
        return await self.add_org_with_options_async(request, headers, runtime)

    def add_org_with_options(
        self,
        request: dingtalkexclusive__1__0_models.AddOrgRequest,
        headers: dingtalkexclusive__1__0_models.AddOrgHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.AddOrgResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile_num):
            body['mobileNum'] = request.mobile_num
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.AddOrgResponse(),
            self.do_roarequest('AddOrg', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/orgnizations', 'json', req, runtime)
        )

    async def add_org_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.AddOrgRequest,
        headers: dingtalkexclusive__1__0_models.AddOrgHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.AddOrgResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile_num):
            body['mobileNum'] = request.mobile_num
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.AddOrgResponse(),
            await self.do_roarequest_async('AddOrg', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/orgnizations', 'json', req, runtime)
        )

    def ban_or_open_group_words(
        self,
        request: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest,
    ) -> dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders()
        return self.ban_or_open_group_words_with_options(request, headers, runtime)

    async def ban_or_open_group_words_async(
        self,
        request: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest,
    ) -> dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders()
        return await self.ban_or_open_group_words_with_options_async(request, headers, runtime)

    def ban_or_open_group_words_with_options(
        self,
        request: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest,
        headers: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ban_words_type):
            body['banWordsType'] = request.ban_words_type
        if not UtilClient.is_unset(request.open_converation_id):
            body['openConverationId'] = request.open_converation_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse(),
            self.do_roarequest('BanOrOpenGroupWords', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/enterpriseSecurities/banOrOpenGroupWords', 'json', req, runtime)
        )

    async def ban_or_open_group_words_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest,
        headers: dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ban_words_type):
            body['banWordsType'] = request.ban_words_type
        if not UtilClient.is_unset(request.open_converation_id):
            body['openConverationId'] = request.open_converation_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.BanOrOpenGroupWordsResponse(),
            await self.do_roarequest_async('BanOrOpenGroupWords', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/enterpriseSecurities/banOrOpenGroupWords', 'json', req, runtime)
        )

    def create_trusted_device(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders()
        return self.create_trusted_device_with_options(request, headers, runtime)

    async def create_trusted_device_async(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders()
        return await self.create_trusted_device_with_options_async(request, headers, runtime)

    def create_trusted_device_with_options(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest,
        headers: dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mac_address):
            body['macAddress'] = request.mac_address
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse(),
            self.do_roarequest('CreateTrustedDevice', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trustedDevices', 'json', req, runtime)
        )

    async def create_trusted_device_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest,
        headers: dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mac_address):
            body['macAddress'] = request.mac_address
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.CreateTrustedDeviceResponse(),
            await self.do_roarequest_async('CreateTrustedDevice', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trustedDevices', 'json', req, runtime)
        )

    def create_trusted_device_batch(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders()
        return self.create_trusted_device_batch_with_options(request, headers, runtime)

    async def create_trusted_device_batch_async(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders()
        return await self.create_trusted_device_batch_with_options_async(request, headers, runtime)

    def create_trusted_device_batch_with_options(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest,
        headers: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mac_address_list):
            body['macAddressList'] = request.mac_address_list
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse(),
            self.do_roarequest('CreateTrustedDeviceBatch', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trusts/devices', 'json', req, runtime)
        )

    async def create_trusted_device_batch_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest,
        headers: dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mac_address_list):
            body['macAddressList'] = request.mac_address_list
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchResponse(),
            await self.do_roarequest_async('CreateTrustedDeviceBatch', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trusts/devices', 'json', req, runtime)
        )

    def delete_across_cloud_stroage_configs(
        self,
        target_corp_id: str,
    ) -> dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsHeaders()
        return self.delete_across_cloud_stroage_configs_with_options(target_corp_id, headers, runtime)

    async def delete_across_cloud_stroage_configs_async(
        self,
        target_corp_id: str,
    ) -> dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsHeaders()
        return await self.delete_across_cloud_stroage_configs_with_options_async(target_corp_id, headers, runtime)

    def delete_across_cloud_stroage_configs_with_options(
        self,
        target_corp_id: str,
        headers: dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse:
        target_corp_id = OpenApiUtilClient.get_encode_param(target_corp_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse(),
            self.do_roarequest('DeleteAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations/{target_corp_id}', 'json', req, runtime)
        )

    async def delete_across_cloud_stroage_configs_with_options_async(
        self,
        target_corp_id: str,
        headers: dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse:
        target_corp_id = OpenApiUtilClient.get_encode_param(target_corp_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DeleteAcrossCloudStroageConfigsResponse(),
            await self.do_roarequest_async('DeleteAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations/{target_corp_id}', 'json', req, runtime)
        )

    def delete_comment(
        self,
        publisher_id: str,
        comment_id: str,
    ) -> dingtalkexclusive__1__0_models.DeleteCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DeleteCommentHeaders()
        return self.delete_comment_with_options(publisher_id, comment_id, headers, runtime)

    async def delete_comment_async(
        self,
        publisher_id: str,
        comment_id: str,
    ) -> dingtalkexclusive__1__0_models.DeleteCommentResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DeleteCommentHeaders()
        return await self.delete_comment_with_options_async(publisher_id, comment_id, headers, runtime)

    def delete_comment_with_options(
        self,
        publisher_id: str,
        comment_id: str,
        headers: dingtalkexclusive__1__0_models.DeleteCommentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DeleteCommentResponse:
        publisher_id = OpenApiUtilClient.get_encode_param(publisher_id)
        comment_id = OpenApiUtilClient.get_encode_param(comment_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DeleteCommentResponse(),
            self.do_roarequest('DeleteComment', 'exclusive_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/exclusive/publishers/{publisher_id}/comments/{comment_id}', 'boolean', req, runtime)
        )

    async def delete_comment_with_options_async(
        self,
        publisher_id: str,
        comment_id: str,
        headers: dingtalkexclusive__1__0_models.DeleteCommentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DeleteCommentResponse:
        publisher_id = OpenApiUtilClient.get_encode_param(publisher_id)
        comment_id = OpenApiUtilClient.get_encode_param(comment_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DeleteCommentResponse(),
            await self.do_roarequest_async('DeleteComment', 'exclusive_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/exclusive/publishers/{publisher_id}/comments/{comment_id}', 'boolean', req, runtime)
        )

    def distribute_partner_app(
        self,
        request: dingtalkexclusive__1__0_models.DistributePartnerAppRequest,
    ) -> dingtalkexclusive__1__0_models.DistributePartnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DistributePartnerAppHeaders()
        return self.distribute_partner_app_with_options(request, headers, runtime)

    async def distribute_partner_app_async(
        self,
        request: dingtalkexclusive__1__0_models.DistributePartnerAppRequest,
    ) -> dingtalkexclusive__1__0_models.DistributePartnerAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.DistributePartnerAppHeaders()
        return await self.distribute_partner_app_with_options_async(request, headers, runtime)

    def distribute_partner_app_with_options(
        self,
        request: dingtalkexclusive__1__0_models.DistributePartnerAppRequest,
        headers: dingtalkexclusive__1__0_models.DistributePartnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DistributePartnerAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.sub_corp_id):
            body['subCorpId'] = request.sub_corp_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DistributePartnerAppResponse(),
            self.do_roarequest('DistributePartnerApp', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partners/applications/distribute', 'json', req, runtime)
        )

    async def distribute_partner_app_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.DistributePartnerAppRequest,
        headers: dingtalkexclusive__1__0_models.DistributePartnerAppHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.DistributePartnerAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.sub_corp_id):
            body['subCorpId'] = request.sub_corp_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.DistributePartnerAppResponse(),
            await self.do_roarequest_async('DistributePartnerApp', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partners/applications/distribute', 'json', req, runtime)
        )

    def file_storage_active_storage(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageActiveStorageRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageActiveStorageHeaders()
        return self.file_storage_active_storage_with_options(request, headers, runtime)

    async def file_storage_active_storage_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageActiveStorageRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageActiveStorageHeaders()
        return await self.file_storage_active_storage_with_options_async(request, headers, runtime)

    def file_storage_active_storage_with_options(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageActiveStorageRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageActiveStorageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.oss):
            body['oss'] = request.oss
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse(),
            self.do_roarequest('FileStorageActiveStorage', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/active', 'json', req, runtime)
        )

    async def file_storage_active_storage_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageActiveStorageRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageActiveStorageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.oss):
            body['oss'] = request.oss
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageActiveStorageResponse(),
            await self.do_roarequest_async('FileStorageActiveStorage', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/active', 'json', req, runtime)
        )

    def file_storage_check_connection(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageCheckConnectionRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageCheckConnectionHeaders()
        return self.file_storage_check_connection_with_options(request, headers, runtime)

    async def file_storage_check_connection_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageCheckConnectionRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageCheckConnectionHeaders()
        return await self.file_storage_check_connection_with_options_async(request, headers, runtime)

    def file_storage_check_connection_with_options(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageCheckConnectionRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageCheckConnectionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.oss):
            body['oss'] = request.oss
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse(),
            self.do_roarequest('FileStorageCheckConnection', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/connections/check', 'json', req, runtime)
        )

    async def file_storage_check_connection_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageCheckConnectionRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageCheckConnectionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.oss):
            body['oss'] = request.oss
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageCheckConnectionResponse(),
            await self.do_roarequest_async('FileStorageCheckConnection', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/connections/check', 'json', req, runtime)
        )

    def file_storage_get_quota_data(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageGetQuotaDataHeaders()
        return self.file_storage_get_quota_data_with_options(request, headers, runtime)

    async def file_storage_get_quota_data_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageGetQuotaDataHeaders()
        return await self.file_storage_get_quota_data_with_options_async(request, headers, runtime)

    def file_storage_get_quota_data_with_options(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse(),
            self.do_roarequest('FileStorageGetQuotaData', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/quotaDatas', 'json', req, runtime)
        )

    async def file_storage_get_quota_data_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageGetQuotaDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageGetQuotaDataResponse(),
            await self.do_roarequest_async('FileStorageGetQuotaData', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/quotaDatas', 'json', req, runtime)
        )

    def file_storage_get_storage_state(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetStorageStateRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageGetStorageStateHeaders()
        return self.file_storage_get_storage_state_with_options(request, headers, runtime)

    async def file_storage_get_storage_state_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetStorageStateRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageGetStorageStateHeaders()
        return await self.file_storage_get_storage_state_with_options_async(request, headers, runtime)

    def file_storage_get_storage_state_with_options(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetStorageStateRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageGetStorageStateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse(),
            self.do_roarequest('FileStorageGetStorageState', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/states', 'json', req, runtime)
        )

    async def file_storage_get_storage_state_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageGetStorageStateRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageGetStorageStateHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageGetStorageStateResponse(),
            await self.do_roarequest_async('FileStorageGetStorageState', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/states', 'json', req, runtime)
        )

    def file_storage_update_storage(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageUpdateStorageRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageUpdateStorageHeaders()
        return self.file_storage_update_storage_with_options(request, headers, runtime)

    async def file_storage_update_storage_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageUpdateStorageRequest,
    ) -> dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.FileStorageUpdateStorageHeaders()
        return await self.file_storage_update_storage_with_options_async(request, headers, runtime)

    def file_storage_update_storage_with_options(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageUpdateStorageRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageUpdateStorageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse(),
            self.do_roarequest('FileStorageUpdateStorage', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/fileStorages/configurations', 'json', req, runtime)
        )

    async def file_storage_update_storage_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.FileStorageUpdateStorageRequest,
        headers: dingtalkexclusive__1__0_models.FileStorageUpdateStorageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.FileStorageUpdateStorageResponse(),
            await self.do_roarequest_async('FileStorageUpdateStorage', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/fileStorages/configurations', 'json', req, runtime)
        )

    def get_active_user_summary(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetActiveUserSummaryHeaders()
        return self.get_active_user_summary_with_options(data_id, headers, runtime)

    async def get_active_user_summary_async(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetActiveUserSummaryHeaders()
        return await self.get_active_user_summary_with_options_async(data_id, headers, runtime)

    def get_active_user_summary_with_options(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetActiveUserSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse(),
            self.do_roarequest('GetActiveUserSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/dau/org/{data_id}', 'json', req, runtime)
        )

    async def get_active_user_summary_with_options_async(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetActiveUserSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetActiveUserSummaryResponse(),
            await self.do_roarequest_async('GetActiveUserSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/dau/org/{data_id}', 'json', req, runtime)
        )

    def get_all_labelable_depts(self) -> dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetAllLabelableDeptsHeaders()
        return self.get_all_labelable_depts_with_options(headers, runtime)

    async def get_all_labelable_depts_async(self) -> dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetAllLabelableDeptsHeaders()
        return await self.get_all_labelable_depts_with_options_async(headers, runtime)

    def get_all_labelable_depts_with_options(
        self,
        headers: dingtalkexclusive__1__0_models.GetAllLabelableDeptsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse(),
            self.do_roarequest('GetAllLabelableDepts', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partnerDepartments', 'json', req, runtime)
        )

    async def get_all_labelable_depts_with_options_async(
        self,
        headers: dingtalkexclusive__1__0_models.GetAllLabelableDeptsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse:
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetAllLabelableDeptsResponse(),
            await self.do_roarequest_async('GetAllLabelableDepts', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partnerDepartments', 'json', req, runtime)
        )

    def get_calender_summary(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetCalenderSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetCalenderSummaryHeaders()
        return self.get_calender_summary_with_options(data_id, headers, runtime)

    async def get_calender_summary_async(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetCalenderSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetCalenderSummaryHeaders()
        return await self.get_calender_summary_with_options_async(data_id, headers, runtime)

    def get_calender_summary_with_options(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetCalenderSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetCalenderSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetCalenderSummaryResponse(),
            self.do_roarequest('GetCalenderSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/calendar/org/{data_id}', 'json', req, runtime)
        )

    async def get_calender_summary_with_options_async(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetCalenderSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetCalenderSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetCalenderSummaryResponse(),
            await self.do_roarequest_async('GetCalenderSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/calendar/org/{data_id}', 'json', req, runtime)
        )

    def get_comment_list(
        self,
        publisher_id: str,
        request: dingtalkexclusive__1__0_models.GetCommentListRequest,
    ) -> dingtalkexclusive__1__0_models.GetCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetCommentListHeaders()
        return self.get_comment_list_with_options(publisher_id, request, headers, runtime)

    async def get_comment_list_async(
        self,
        publisher_id: str,
        request: dingtalkexclusive__1__0_models.GetCommentListRequest,
    ) -> dingtalkexclusive__1__0_models.GetCommentListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetCommentListHeaders()
        return await self.get_comment_list_with_options_async(publisher_id, request, headers, runtime)

    def get_comment_list_with_options(
        self,
        publisher_id: str,
        request: dingtalkexclusive__1__0_models.GetCommentListRequest,
        headers: dingtalkexclusive__1__0_models.GetCommentListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetCommentListResponse:
        UtilClient.validate_model(request)
        publisher_id = OpenApiUtilClient.get_encode_param(publisher_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetCommentListResponse(),
            self.do_roarequest('GetCommentList', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/publishers/{publisher_id}/comments/list', 'json', req, runtime)
        )

    async def get_comment_list_with_options_async(
        self,
        publisher_id: str,
        request: dingtalkexclusive__1__0_models.GetCommentListRequest,
        headers: dingtalkexclusive__1__0_models.GetCommentListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetCommentListResponse:
        UtilClient.validate_model(request)
        publisher_id = OpenApiUtilClient.get_encode_param(publisher_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetCommentListResponse(),
            await self.do_roarequest_async('GetCommentList', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/publishers/{publisher_id}/comments/list', 'json', req, runtime)
        )

    def get_conference_detail(
        self,
        conference_id: str,
    ) -> dingtalkexclusive__1__0_models.GetConferenceDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetConferenceDetailHeaders()
        return self.get_conference_detail_with_options(conference_id, headers, runtime)

    async def get_conference_detail_async(
        self,
        conference_id: str,
    ) -> dingtalkexclusive__1__0_models.GetConferenceDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetConferenceDetailHeaders()
        return await self.get_conference_detail_with_options_async(conference_id, headers, runtime)

    def get_conference_detail_with_options(
        self,
        conference_id: str,
        headers: dingtalkexclusive__1__0_models.GetConferenceDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetConferenceDetailResponse:
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetConferenceDetailResponse(),
            self.do_roarequest('GetConferenceDetail', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/conferences/{conference_id}', 'json', req, runtime)
        )

    async def get_conference_detail_with_options_async(
        self,
        conference_id: str,
        headers: dingtalkexclusive__1__0_models.GetConferenceDetailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetConferenceDetailResponse:
        conference_id = OpenApiUtilClient.get_encode_param(conference_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetConferenceDetailResponse(),
            await self.do_roarequest_async('GetConferenceDetail', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/conferences/{conference_id}', 'json', req, runtime)
        )

    def get_ding_report_dept_summary(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDingReportDeptSummaryHeaders()
        return self.get_ding_report_dept_summary_with_options(data_id, request, headers, runtime)

    async def get_ding_report_dept_summary_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDingReportDeptSummaryHeaders()
        return await self.get_ding_report_dept_summary_with_options_async(data_id, request, headers, runtime)

    def get_ding_report_dept_summary_with_options(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse(),
            self.do_roarequest('GetDingReportDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/report/dept/{data_id}', 'json', req, runtime)
        )

    async def get_ding_report_dept_summary_with_options_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetDingReportDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDingReportDeptSummaryResponse(),
            await self.do_roarequest_async('GetDingReportDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/report/dept/{data_id}', 'json', req, runtime)
        )

    def get_ding_report_summary(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetDingReportSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDingReportSummaryHeaders()
        return self.get_ding_report_summary_with_options(data_id, headers, runtime)

    async def get_ding_report_summary_async(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetDingReportSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDingReportSummaryHeaders()
        return await self.get_ding_report_summary_with_options_async(data_id, headers, runtime)

    def get_ding_report_summary_with_options(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetDingReportSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDingReportSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDingReportSummaryResponse(),
            self.do_roarequest('GetDingReportSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/datas/{data_id}/reports/organizations', 'json', req, runtime)
        )

    async def get_ding_report_summary_with_options_async(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetDingReportSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDingReportSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDingReportSummaryResponse(),
            await self.do_roarequest_async('GetDingReportSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/datas/{data_id}/reports/organizations', 'json', req, runtime)
        )

    def get_doc_created_dept_summary(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryHeaders()
        return self.get_doc_created_dept_summary_with_options(data_id, request, headers, runtime)

    async def get_doc_created_dept_summary_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryHeaders()
        return await self.get_doc_created_dept_summary_with_options_async(data_id, request, headers, runtime)

    def get_doc_created_dept_summary_with_options(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse(),
            self.do_roarequest('GetDocCreatedDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/doc/dept/{data_id}', 'json', req, runtime)
        )

    async def get_doc_created_dept_summary_with_options_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDocCreatedDeptSummaryResponse(),
            await self.do_roarequest_async('GetDocCreatedDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/doc/dept/{data_id}', 'json', req, runtime)
        )

    def get_doc_created_summary(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDocCreatedSummaryHeaders()
        return self.get_doc_created_summary_with_options(data_id, headers, runtime)

    async def get_doc_created_summary_async(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetDocCreatedSummaryHeaders()
        return await self.get_doc_created_summary_with_options_async(data_id, headers, runtime)

    def get_doc_created_summary_with_options(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetDocCreatedSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse(),
            self.do_roarequest('GetDocCreatedSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/doc/org/{data_id}', 'json', req, runtime)
        )

    async def get_doc_created_summary_with_options_async(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetDocCreatedSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetDocCreatedSummaryResponse(),
            await self.do_roarequest_async('GetDocCreatedSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/doc/org/{data_id}', 'json', req, runtime)
        )

    def get_general_form_created_dept_summary(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryHeaders()
        return self.get_general_form_created_dept_summary_with_options(data_id, request, headers, runtime)

    async def get_general_form_created_dept_summary_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryHeaders()
        return await self.get_general_form_created_dept_summary_with_options_async(data_id, request, headers, runtime)

    def get_general_form_created_dept_summary_with_options(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse(),
            self.do_roarequest('GetGeneralFormCreatedDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/generalForm/dept/{data_id}', 'json', req, runtime)
        )

    async def get_general_form_created_dept_summary_with_options_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGeneralFormCreatedDeptSummaryResponse(),
            await self.do_roarequest_async('GetGeneralFormCreatedDeptSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/generalForm/dept/{data_id}', 'json', req, runtime)
        )

    def get_general_form_created_summary(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryHeaders()
        return self.get_general_form_created_summary_with_options(data_id, headers, runtime)

    async def get_general_form_created_summary_async(
        self,
        data_id: str,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryHeaders()
        return await self.get_general_form_created_summary_with_options_async(data_id, headers, runtime)

    def get_general_form_created_summary_with_options(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse(),
            self.do_roarequest('GetGeneralFormCreatedSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/generalForm/org/{data_id}', 'json', req, runtime)
        )

    async def get_general_form_created_summary_with_options_async(
        self,
        data_id: str,
        headers: dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse:
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGeneralFormCreatedSummaryResponse(),
            await self.do_roarequest_async('GetGeneralFormCreatedSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/generalForm/org/{data_id}', 'json', req, runtime)
        )

    def get_group_active_info(
        self,
        request: dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest,
    ) -> dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders()
        return self.get_group_active_info_with_options(request, headers, runtime)

    async def get_group_active_info_async(
        self,
        request: dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest,
    ) -> dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders()
        return await self.get_group_active_info_with_options_async(request, headers, runtime)

    def get_group_active_info_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest,
        headers: dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ding_group_id):
            query['dingGroupId'] = request.ding_group_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_date):
            query['statDate'] = request.stat_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse(),
            self.do_roarequest('GetGroupActiveInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/activeGroups', 'json', req, runtime)
        )

    async def get_group_active_info_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest,
        headers: dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ding_group_id):
            query['dingGroupId'] = request.ding_group_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_date):
            query['statDate'] = request.stat_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetGroupActiveInfoResponse(),
            await self.do_roarequest_async('GetGroupActiveInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/activeGroups', 'json', req, runtime)
        )

    def get_in_active_user_list(
        self,
        request: dingtalkexclusive__1__0_models.GetInActiveUserListRequest,
    ) -> dingtalkexclusive__1__0_models.GetInActiveUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetInActiveUserListHeaders()
        return self.get_in_active_user_list_with_options(request, headers, runtime)

    async def get_in_active_user_list_async(
        self,
        request: dingtalkexclusive__1__0_models.GetInActiveUserListRequest,
    ) -> dingtalkexclusive__1__0_models.GetInActiveUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetInActiveUserListHeaders()
        return await self.get_in_active_user_list_with_options_async(request, headers, runtime)

    def get_in_active_user_list_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetInActiveUserListRequest,
        headers: dingtalkexclusive__1__0_models.GetInActiveUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetInActiveUserListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_date):
            body['statDate'] = request.stat_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetInActiveUserListResponse(),
            self.do_roarequest('GetInActiveUserList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/inactives/users/query', 'json', req, runtime)
        )

    async def get_in_active_user_list_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetInActiveUserListRequest,
        headers: dingtalkexclusive__1__0_models.GetInActiveUserListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetInActiveUserListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_date):
            body['statDate'] = request.stat_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetInActiveUserListResponse(),
            await self.do_roarequest_async('GetInActiveUserList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/inactives/users/query', 'json', req, runtime)
        )

    def get_last_org_auth_data(
        self,
        request: dingtalkexclusive__1__0_models.GetLastOrgAuthDataRequest,
    ) -> dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetLastOrgAuthDataHeaders()
        return self.get_last_org_auth_data_with_options(request, headers, runtime)

    async def get_last_org_auth_data_async(
        self,
        request: dingtalkexclusive__1__0_models.GetLastOrgAuthDataRequest,
    ) -> dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetLastOrgAuthDataHeaders()
        return await self.get_last_org_auth_data_with_options_async(request, headers, runtime)

    def get_last_org_auth_data_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetLastOrgAuthDataRequest,
        headers: dingtalkexclusive__1__0_models.GetLastOrgAuthDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse(),
            self.do_roarequest('GetLastOrgAuthData', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/organizations/authInfos', 'json', req, runtime)
        )

    async def get_last_org_auth_data_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetLastOrgAuthDataRequest,
        headers: dingtalkexclusive__1__0_models.GetLastOrgAuthDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetLastOrgAuthDataResponse(),
            await self.do_roarequest_async('GetLastOrgAuthData', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/organizations/authInfos', 'json', req, runtime)
        )

    def get_oa_operator_log_list(
        self,
        request: dingtalkexclusive__1__0_models.GetOaOperatorLogListRequest,
    ) -> dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetOaOperatorLogListHeaders()
        return self.get_oa_operator_log_list_with_options(request, headers, runtime)

    async def get_oa_operator_log_list_async(
        self,
        request: dingtalkexclusive__1__0_models.GetOaOperatorLogListRequest,
    ) -> dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetOaOperatorLogListHeaders()
        return await self.get_oa_operator_log_list_with_options_async(request, headers, runtime)

    def get_oa_operator_log_list_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetOaOperatorLogListRequest,
        headers: dingtalkexclusive__1__0_models.GetOaOperatorLogListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_list):
            body['categoryList'] = request.category_list
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse(),
            self.do_roarequest('GetOaOperatorLogList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/oaOperatorLogs/query', 'json', req, runtime)
        )

    async def get_oa_operator_log_list_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetOaOperatorLogListRequest,
        headers: dingtalkexclusive__1__0_models.GetOaOperatorLogListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_list):
            body['categoryList'] = request.category_list
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_id):
            body['opUserId'] = request.op_user_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetOaOperatorLogListResponse(),
            await self.do_roarequest_async('GetOaOperatorLogList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/oaOperatorLogs/query', 'json', req, runtime)
        )

    def get_partner_type_by_parent_id(
        self,
        parent_id: str,
    ) -> dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdHeaders()
        return self.get_partner_type_by_parent_id_with_options(parent_id, headers, runtime)

    async def get_partner_type_by_parent_id_async(
        self,
        parent_id: str,
    ) -> dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdHeaders()
        return await self.get_partner_type_by_parent_id_with_options_async(parent_id, headers, runtime)

    def get_partner_type_by_parent_id_with_options(
        self,
        parent_id: str,
        headers: dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse:
        parent_id = OpenApiUtilClient.get_encode_param(parent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse(),
            self.do_roarequest('GetPartnerTypeByParentId', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partnerLabels/{parent_id}', 'json', req, runtime)
        )

    async def get_partner_type_by_parent_id_with_options_async(
        self,
        parent_id: str,
        headers: dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse:
        parent_id = OpenApiUtilClient.get_encode_param(parent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetPartnerTypeByParentIdResponse(),
            await self.do_roarequest_async('GetPartnerTypeByParentId', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partnerLabels/{parent_id}', 'json', req, runtime)
        )

    def get_publisher_summary(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetPublisherSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetPublisherSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetPublisherSummaryHeaders()
        return self.get_publisher_summary_with_options(data_id, request, headers, runtime)

    async def get_publisher_summary_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetPublisherSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetPublisherSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetPublisherSummaryHeaders()
        return await self.get_publisher_summary_with_options_async(data_id, request, headers, runtime)

    def get_publisher_summary_with_options(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetPublisherSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetPublisherSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetPublisherSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetPublisherSummaryResponse(),
            self.do_roarequest('GetPublisherSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/publisher/{data_id}', 'json', req, runtime)
        )

    async def get_publisher_summary_with_options_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetPublisherSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetPublisherSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetPublisherSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetPublisherSummaryResponse(),
            await self.do_roarequest_async('GetPublisherSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/publisher/{data_id}', 'json', req, runtime)
        )

    def get_signed_detail_by_page(
        self,
        request: dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest,
    ) -> dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders()
        return self.get_signed_detail_by_page_with_options(request, headers, runtime)

    async def get_signed_detail_by_page_async(
        self,
        request: dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest,
    ) -> dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders()
        return await self.get_signed_detail_by_page_with_options_async(request, headers, runtime)

    def get_signed_detail_by_page_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest,
        headers: dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sign_status):
            query['signStatus'] = request.sign_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse(),
            self.do_roarequest('GetSignedDetailByPage', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/audits/users', 'json', req, runtime)
        )

    async def get_signed_detail_by_page_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest,
        headers: dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sign_status):
            query['signStatus'] = request.sign_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetSignedDetailByPageResponse(),
            await self.do_roarequest_async('GetSignedDetailByPage', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/audits/users', 'json', req, runtime)
        )

    def get_trust_device_list(
        self,
        request: dingtalkexclusive__1__0_models.GetTrustDeviceListRequest,
    ) -> dingtalkexclusive__1__0_models.GetTrustDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders()
        return self.get_trust_device_list_with_options(request, headers, runtime)

    async def get_trust_device_list_async(
        self,
        request: dingtalkexclusive__1__0_models.GetTrustDeviceListRequest,
    ) -> dingtalkexclusive__1__0_models.GetTrustDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders()
        return await self.get_trust_device_list_with_options_async(request, headers, runtime)

    def get_trust_device_list_with_options(
        self,
        request: dingtalkexclusive__1__0_models.GetTrustDeviceListRequest,
        headers: dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetTrustDeviceListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetTrustDeviceListResponse(),
            self.do_roarequest('GetTrustDeviceList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trustedDevices/query', 'json', req, runtime)
        )

    async def get_trust_device_list_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.GetTrustDeviceListRequest,
        headers: dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetTrustDeviceListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetTrustDeviceListResponse(),
            await self.do_roarequest_async('GetTrustDeviceList', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/trustedDevices/query', 'json', req, runtime)
        )

    def get_user_app_version_summary(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetUserAppVersionSummaryHeaders()
        return self.get_user_app_version_summary_with_options(data_id, request, headers, runtime)

    async def get_user_app_version_summary_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryRequest,
    ) -> dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.GetUserAppVersionSummaryHeaders()
        return await self.get_user_app_version_summary_with_options_async(data_id, request, headers, runtime)

    def get_user_app_version_summary_with_options(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse(),
            self.do_roarequest('GetUserAppVersionSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/appVersion/org/{data_id}', 'json', req, runtime)
        )

    async def get_user_app_version_summary_with_options_async(
        self,
        data_id: str,
        request: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryRequest,
        headers: dingtalkexclusive__1__0_models.GetUserAppVersionSummaryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse:
        UtilClient.validate_model(request)
        data_id = OpenApiUtilClient.get_encode_param(data_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.GetUserAppVersionSummaryResponse(),
            await self.do_roarequest_async('GetUserAppVersionSummary', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/data/appVersion/org/{data_id}', 'json', req, runtime)
        )

    def list_audit_log(
        self,
        request: dingtalkexclusive__1__0_models.ListAuditLogRequest,
    ) -> dingtalkexclusive__1__0_models.ListAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListAuditLogHeaders()
        return self.list_audit_log_with_options(request, headers, runtime)

    async def list_audit_log_async(
        self,
        request: dingtalkexclusive__1__0_models.ListAuditLogRequest,
    ) -> dingtalkexclusive__1__0_models.ListAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListAuditLogHeaders()
        return await self.list_audit_log_with_options_async(request, headers, runtime)

    def list_audit_log_with_options(
        self,
        request: dingtalkexclusive__1__0_models.ListAuditLogRequest,
        headers: dingtalkexclusive__1__0_models.ListAuditLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.next_biz_id):
            query['nextBizId'] = request.next_biz_id
        if not UtilClient.is_unset(request.next_gmt_create):
            query['nextGmtCreate'] = request.next_gmt_create
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListAuditLogResponse(),
            self.do_roarequest('ListAuditLog', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileAuditLogs', 'json', req, runtime)
        )

    async def list_audit_log_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.ListAuditLogRequest,
        headers: dingtalkexclusive__1__0_models.ListAuditLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.next_biz_id):
            query['nextBizId'] = request.next_biz_id
        if not UtilClient.is_unset(request.next_gmt_create):
            query['nextGmtCreate'] = request.next_gmt_create
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListAuditLogResponse(),
            await self.do_roarequest_async('ListAuditLog', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileAuditLogs', 'json', req, runtime)
        )

    def list_join_org_info(
        self,
        request: dingtalkexclusive__1__0_models.ListJoinOrgInfoRequest,
    ) -> dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListJoinOrgInfoHeaders()
        return self.list_join_org_info_with_options(request, headers, runtime)

    async def list_join_org_info_async(
        self,
        request: dingtalkexclusive__1__0_models.ListJoinOrgInfoRequest,
    ) -> dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListJoinOrgInfoHeaders()
        return await self.list_join_org_info_with_options_async(request, headers, runtime)

    def list_join_org_info_with_options(
        self,
        request: dingtalkexclusive__1__0_models.ListJoinOrgInfoRequest,
        headers: dingtalkexclusive__1__0_models.ListJoinOrgInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobile):
            query['mobile'] = request.mobile
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse(),
            self.do_roarequest('ListJoinOrgInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/exclusiveAccounts/organizations/infos', 'json', req, runtime)
        )

    async def list_join_org_info_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.ListJoinOrgInfoRequest,
        headers: dingtalkexclusive__1__0_models.ListJoinOrgInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobile):
            query['mobile'] = request.mobile
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListJoinOrgInfoResponse(),
            await self.do_roarequest_async('ListJoinOrgInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/exclusiveAccounts/organizations/infos', 'json', req, runtime)
        )

    def list_mini_app_available_version(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionRequest,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionHeaders()
        return self.list_mini_app_available_version_with_options(request, headers, runtime)

    async def list_mini_app_available_version_async(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionRequest,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionHeaders()
        return await self.list_mini_app_available_version_with_options_async(request, headers, runtime)

    def list_mini_app_available_version_with_options(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionRequest,
        headers: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_type_set):
            body['versionTypeSet'] = request.version_type_set
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse(),
            self.do_roarequest('ListMiniAppAvailableVersion', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/availableLists', 'json', req, runtime)
        )

    async def list_mini_app_available_version_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionRequest,
        headers: dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_type_set):
            body['versionTypeSet'] = request.version_type_set
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListMiniAppAvailableVersionResponse(),
            await self.do_roarequest_async('ListMiniAppAvailableVersion', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/availableLists', 'json', req, runtime)
        )

    def list_mini_app_history_version(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionRequest,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionHeaders()
        return self.list_mini_app_history_version_with_options(request, headers, runtime)

    async def list_mini_app_history_version_async(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionRequest,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionHeaders()
        return await self.list_mini_app_history_version_with_options_async(request, headers, runtime)

    def list_mini_app_history_version_with_options(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionRequest,
        headers: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse(),
            self.do_roarequest('ListMiniAppHistoryVersion', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/miniApps/versions/historyLists', 'json', req, runtime)
        )

    async def list_mini_app_history_version_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionRequest,
        headers: dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mini_app_id):
            query['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListMiniAppHistoryVersionResponse(),
            await self.do_roarequest_async('ListMiniAppHistoryVersion', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/miniApps/versions/historyLists', 'json', req, runtime)
        )

    def list_partner_roles(
        self,
        parent_id: str,
    ) -> dingtalkexclusive__1__0_models.ListPartnerRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListPartnerRolesHeaders()
        return self.list_partner_roles_with_options(parent_id, headers, runtime)

    async def list_partner_roles_async(
        self,
        parent_id: str,
    ) -> dingtalkexclusive__1__0_models.ListPartnerRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListPartnerRolesHeaders()
        return await self.list_partner_roles_with_options_async(parent_id, headers, runtime)

    def list_partner_roles_with_options(
        self,
        parent_id: str,
        headers: dingtalkexclusive__1__0_models.ListPartnerRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListPartnerRolesResponse:
        parent_id = OpenApiUtilClient.get_encode_param(parent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListPartnerRolesResponse(),
            self.do_roarequest('ListPartnerRoles', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partners/roles/{parent_id}', 'json', req, runtime)
        )

    async def list_partner_roles_with_options_async(
        self,
        parent_id: str,
        headers: dingtalkexclusive__1__0_models.ListPartnerRolesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListPartnerRolesResponse:
        parent_id = OpenApiUtilClient.get_encode_param(parent_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListPartnerRolesResponse(),
            await self.do_roarequest_async('ListPartnerRoles', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/partners/roles/{parent_id}', 'json', req, runtime)
        )

    def list_punch_schedule_by_condition_with_paging(
        self,
        request: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingRequest,
    ) -> dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingHeaders()
        return self.list_punch_schedule_by_condition_with_paging_with_options(request, headers, runtime)

    async def list_punch_schedule_by_condition_with_paging_async(
        self,
        request: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingRequest,
    ) -> dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingHeaders()
        return await self.list_punch_schedule_by_condition_with_paging_with_options_async(request, headers, runtime)

    def list_punch_schedule_by_condition_with_paging_with_options(
        self,
        request: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingRequest,
        headers: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_instance_id):
            body['bizInstanceId'] = request.biz_instance_id
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.schedule_date_end):
            body['scheduleDateEnd'] = request.schedule_date_end
        if not UtilClient.is_unset(request.schedule_date_start):
            body['scheduleDateStart'] = request.schedule_date_start
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse(),
            self.do_roarequest('ListPunchScheduleByConditionWithPaging', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/punchSchedules/query', 'json', req, runtime)
        )

    async def list_punch_schedule_by_condition_with_paging_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingRequest,
        headers: dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_instance_id):
            body['bizInstanceId'] = request.biz_instance_id
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.schedule_date_end):
            body['scheduleDateEnd'] = request.schedule_date_end
        if not UtilClient.is_unset(request.schedule_date_start):
            body['scheduleDateStart'] = request.schedule_date_start
        if not UtilClient.is_unset(request.user_id_list):
            body['userIdList'] = request.user_id_list
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.ListPunchScheduleByConditionWithPagingResponse(),
            await self.do_roarequest_async('ListPunchScheduleByConditionWithPaging', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/punchSchedules/query', 'json', req, runtime)
        )

    def publish_file_change_notice(
        self,
        request: dingtalkexclusive__1__0_models.PublishFileChangeNoticeRequest,
    ) -> dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.PublishFileChangeNoticeHeaders()
        return self.publish_file_change_notice_with_options(request, headers, runtime)

    async def publish_file_change_notice_async(
        self,
        request: dingtalkexclusive__1__0_models.PublishFileChangeNoticeRequest,
    ) -> dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.PublishFileChangeNoticeHeaders()
        return await self.publish_file_change_notice_with_options_async(request, headers, runtime)

    def publish_file_change_notice_with_options(
        self,
        request: dingtalkexclusive__1__0_models.PublishFileChangeNoticeRequest,
        headers: dingtalkexclusive__1__0_models.PublishFileChangeNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['fileId'] = request.file_id
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator_union_id):
            body['operatorUnionId'] = request.operator_union_id
        if not UtilClient.is_unset(request.space_id):
            body['spaceId'] = request.space_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse(),
            self.do_roarequest('PublishFileChangeNotice', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/comments/send', 'none', req, runtime)
        )

    async def publish_file_change_notice_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.PublishFileChangeNoticeRequest,
        headers: dingtalkexclusive__1__0_models.PublishFileChangeNoticeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['fileId'] = request.file_id
        if not UtilClient.is_unset(request.operate_type):
            body['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator_union_id):
            body['operatorUnionId'] = request.operator_union_id
        if not UtilClient.is_unset(request.space_id):
            body['spaceId'] = request.space_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.PublishFileChangeNoticeResponse(),
            await self.do_roarequest_async('PublishFileChangeNotice', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/comments/send', 'none', req, runtime)
        )

    def query_across_cloud_stroage_configs(
        self,
        request: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsRequest,
    ) -> dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsHeaders()
        return self.query_across_cloud_stroage_configs_with_options(request, headers, runtime)

    async def query_across_cloud_stroage_configs_async(
        self,
        request: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsRequest,
    ) -> dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsHeaders()
        return await self.query_across_cloud_stroage_configs_with_options_async(request, headers, runtime)

    def query_across_cloud_stroage_configs_with_options(
        self,
        request: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsRequest,
        headers: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_cloud_type):
            query['targetCloudType'] = request.target_cloud_type
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse(),
            self.do_roarequest('QueryAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations', 'json', req, runtime)
        )

    async def query_across_cloud_stroage_configs_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsRequest,
        headers: dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_cloud_type):
            query['targetCloudType'] = request.target_cloud_type
        if not UtilClient.is_unset(request.target_corp_id):
            query['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.QueryAcrossCloudStroageConfigsResponse(),
            await self.do_roarequest_async('QueryAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations', 'json', req, runtime)
        )

    def rollback_mini_app_version(
        self,
        request: dingtalkexclusive__1__0_models.RollbackMiniAppVersionRequest,
    ) -> dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.RollbackMiniAppVersionHeaders()
        return self.rollback_mini_app_version_with_options(request, headers, runtime)

    async def rollback_mini_app_version_async(
        self,
        request: dingtalkexclusive__1__0_models.RollbackMiniAppVersionRequest,
    ) -> dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.RollbackMiniAppVersionHeaders()
        return await self.rollback_mini_app_version_with_options_async(request, headers, runtime)

    def rollback_mini_app_version_with_options(
        self,
        request: dingtalkexclusive__1__0_models.RollbackMiniAppVersionRequest,
        headers: dingtalkexclusive__1__0_models.RollbackMiniAppVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.rollback_version):
            body['rollbackVersion'] = request.rollback_version
        if not UtilClient.is_unset(request.target_version):
            body['targetVersion'] = request.target_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse(),
            self.do_roarequest('RollbackMiniAppVersion', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/rollback', 'json', req, runtime)
        )

    async def rollback_mini_app_version_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.RollbackMiniAppVersionRequest,
        headers: dingtalkexclusive__1__0_models.RollbackMiniAppVersionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.rollback_version):
            body['rollbackVersion'] = request.rollback_version
        if not UtilClient.is_unset(request.target_version):
            body['targetVersion'] = request.target_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.RollbackMiniAppVersionResponse(),
            await self.do_roarequest_async('RollbackMiniAppVersion', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/rollback', 'json', req, runtime)
        )

    def save_across_cloud_stroage_configs(
        self,
        request: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsRequest,
    ) -> dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsHeaders()
        return self.save_across_cloud_stroage_configs_with_options(request, headers, runtime)

    async def save_across_cloud_stroage_configs_async(
        self,
        request: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsRequest,
    ) -> dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsHeaders()
        return await self.save_across_cloud_stroage_configs_with_options_async(request, headers, runtime)

    def save_across_cloud_stroage_configs_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsRequest,
        headers: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.bucket_name):
            body['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.endpoint):
            body['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse(),
            self.do_roarequest('SaveAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations', 'json', req, runtime)
        )

    async def save_across_cloud_stroage_configs_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsRequest,
        headers: dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.bucket_name):
            body['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.cloud_type):
            body['cloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.endpoint):
            body['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SaveAcrossCloudStroageConfigsResponse(),
            await self.do_roarequest_async('SaveAcrossCloudStroageConfigs', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/configurations', 'json', req, runtime)
        )

    def save_and_submit_auth_info(
        self,
        request: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoRequest,
    ) -> dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoHeaders()
        return self.save_and_submit_auth_info_with_options(request, headers, runtime)

    async def save_and_submit_auth_info_async(
        self,
        request: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoRequest,
    ) -> dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoHeaders()
        return await self.save_and_submit_auth_info_with_options_async(request, headers, runtime)

    def save_and_submit_auth_info_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoRequest,
        headers: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_remark):
            body['applyRemark'] = request.apply_remark
        if not UtilClient.is_unset(request.authorize_media_id):
            body['authorizeMediaId'] = request.authorize_media_id
        if not UtilClient.is_unset(request.industry):
            body['industry'] = request.industry
        if not UtilClient.is_unset(request.legal_person):
            body['legalPerson'] = request.legal_person
        if not UtilClient.is_unset(request.legal_person_id_card):
            body['legalPersonIdCard'] = request.legal_person_id_card
        if not UtilClient.is_unset(request.license_media_id):
            body['licenseMediaId'] = request.license_media_id
        if not UtilClient.is_unset(request.loc_city_name):
            body['locCityName'] = request.loc_city_name
        if not UtilClient.is_unset(request.loc_province_name):
            body['locProvinceName'] = request.loc_province_name
        if not UtilClient.is_unset(request.mobile_num):
            body['mobileNum'] = request.mobile_num
        if not UtilClient.is_unset(request.org_name):
            body['orgName'] = request.org_name
        if not UtilClient.is_unset(request.organization_code):
            body['organizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.organization_code_media_id):
            body['organizationCodeMediaId'] = request.organization_code_media_id
        if not UtilClient.is_unset(request.regist_location):
            body['registLocation'] = request.regist_location
        if not UtilClient.is_unset(request.regist_num):
            body['registNum'] = request.regist_num
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.unified_social_credit):
            body['unifiedSocialCredit'] = request.unified_social_credit
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse(),
            self.do_roarequest('SaveAndSubmitAuthInfo', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/ognizations/authInfos/saveAndSubmit', 'json', req, runtime)
        )

    async def save_and_submit_auth_info_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoRequest,
        headers: dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_remark):
            body['applyRemark'] = request.apply_remark
        if not UtilClient.is_unset(request.authorize_media_id):
            body['authorizeMediaId'] = request.authorize_media_id
        if not UtilClient.is_unset(request.industry):
            body['industry'] = request.industry
        if not UtilClient.is_unset(request.legal_person):
            body['legalPerson'] = request.legal_person
        if not UtilClient.is_unset(request.legal_person_id_card):
            body['legalPersonIdCard'] = request.legal_person_id_card
        if not UtilClient.is_unset(request.license_media_id):
            body['licenseMediaId'] = request.license_media_id
        if not UtilClient.is_unset(request.loc_city_name):
            body['locCityName'] = request.loc_city_name
        if not UtilClient.is_unset(request.loc_province_name):
            body['locProvinceName'] = request.loc_province_name
        if not UtilClient.is_unset(request.mobile_num):
            body['mobileNum'] = request.mobile_num
        if not UtilClient.is_unset(request.org_name):
            body['orgName'] = request.org_name
        if not UtilClient.is_unset(request.organization_code):
            body['organizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.organization_code_media_id):
            body['organizationCodeMediaId'] = request.organization_code_media_id
        if not UtilClient.is_unset(request.regist_location):
            body['registLocation'] = request.regist_location
        if not UtilClient.is_unset(request.regist_num):
            body['registNum'] = request.regist_num
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        if not UtilClient.is_unset(request.unified_social_credit):
            body['unifiedSocialCredit'] = request.unified_social_credit
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SaveAndSubmitAuthInfoResponse(),
            await self.do_roarequest_async('SaveAndSubmitAuthInfo', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/ognizations/authInfos/saveAndSubmit', 'json', req, runtime)
        )

    def search_org_inner_group_info(
        self,
        request: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest,
    ) -> dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders()
        return self.search_org_inner_group_info_with_options(request, headers, runtime)

    async def search_org_inner_group_info_async(
        self,
        request: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest,
    ) -> dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders()
        return await self.search_org_inner_group_info_with_options_async(request, headers, runtime)

    def search_org_inner_group_info_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest,
        headers: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['createTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['createTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.group_members_count_end):
            query['groupMembersCountEnd'] = request.group_members_count_end
        if not UtilClient.is_unset(request.group_members_count_start):
            query['groupMembersCountStart'] = request.group_members_count_start
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_owner):
            query['groupOwner'] = request.group_owner
        if not UtilClient.is_unset(request.last_active_time_end):
            query['lastActiveTimeEnd'] = request.last_active_time_end
        if not UtilClient.is_unset(request.last_active_time_start):
            query['lastActiveTimeStart'] = request.last_active_time_start
        if not UtilClient.is_unset(request.operator_user_id):
            query['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_start):
            query['pageStart'] = request.page_start
        if not UtilClient.is_unset(request.sync_to_dingpan):
            query['syncToDingpan'] = request.sync_to_dingpan
        if not UtilClient.is_unset(request.uuid):
            query['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse(),
            self.do_roarequest('SearchOrgInnerGroupInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/securities/orgGroupInfos', 'json', req, runtime)
        )

    async def search_org_inner_group_info_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest,
        headers: dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['createTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['createTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.group_members_count_end):
            query['groupMembersCountEnd'] = request.group_members_count_end
        if not UtilClient.is_unset(request.group_members_count_start):
            query['groupMembersCountStart'] = request.group_members_count_start
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_owner):
            query['groupOwner'] = request.group_owner
        if not UtilClient.is_unset(request.last_active_time_end):
            query['lastActiveTimeEnd'] = request.last_active_time_end
        if not UtilClient.is_unset(request.last_active_time_start):
            query['lastActiveTimeStart'] = request.last_active_time_start
        if not UtilClient.is_unset(request.operator_user_id):
            query['operatorUserId'] = request.operator_user_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_start):
            query['pageStart'] = request.page_start
        if not UtilClient.is_unset(request.sync_to_dingpan):
            query['syncToDingpan'] = request.sync_to_dingpan
        if not UtilClient.is_unset(request.uuid):
            query['uuid'] = request.uuid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoResponse(),
            await self.do_roarequest_async('SearchOrgInnerGroupInfo', 'exclusive_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/exclusive/securities/orgGroupInfos', 'json', req, runtime)
        )

    def send_app_ding(
        self,
        request: dingtalkexclusive__1__0_models.SendAppDingRequest,
    ) -> dingtalkexclusive__1__0_models.SendAppDingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SendAppDingHeaders()
        return self.send_app_ding_with_options(request, headers, runtime)

    async def send_app_ding_async(
        self,
        request: dingtalkexclusive__1__0_models.SendAppDingRequest,
    ) -> dingtalkexclusive__1__0_models.SendAppDingResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SendAppDingHeaders()
        return await self.send_app_ding_with_options_async(request, headers, runtime)

    def send_app_ding_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SendAppDingRequest,
        headers: dingtalkexclusive__1__0_models.SendAppDingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SendAppDingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.userids):
            body['userids'] = request.userids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SendAppDingResponse(),
            self.do_roarequest('SendAppDing', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/appDings/send', 'none', req, runtime)
        )

    async def send_app_ding_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SendAppDingRequest,
        headers: dingtalkexclusive__1__0_models.SendAppDingHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SendAppDingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.userids):
            body['userids'] = request.userids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SendAppDingResponse(),
            await self.do_roarequest_async('SendAppDing', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/appDings/send', 'none', req, runtime)
        )

    def send_invitation(
        self,
        request: dingtalkexclusive__1__0_models.SendInvitationRequest,
    ) -> dingtalkexclusive__1__0_models.SendInvitationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SendInvitationHeaders()
        return self.send_invitation_with_options(request, headers, runtime)

    async def send_invitation_async(
        self,
        request: dingtalkexclusive__1__0_models.SendInvitationRequest,
    ) -> dingtalkexclusive__1__0_models.SendInvitationResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SendInvitationHeaders()
        return await self.send_invitation_with_options_async(request, headers, runtime)

    def send_invitation_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SendInvitationRequest,
        headers: dingtalkexclusive__1__0_models.SendInvitationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SendInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.org_alias):
            body['orgAlias'] = request.org_alias
        if not UtilClient.is_unset(request.partner_label_id):
            body['partnerLabelId'] = request.partner_label_id
        if not UtilClient.is_unset(request.partner_num):
            body['partnerNum'] = request.partner_num
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SendInvitationResponse(),
            self.do_roarequest('SendInvitation', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partnerDepartments/invitations/send', 'none', req, runtime)
        )

    async def send_invitation_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SendInvitationRequest,
        headers: dingtalkexclusive__1__0_models.SendInvitationHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SendInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.org_alias):
            body['orgAlias'] = request.org_alias
        if not UtilClient.is_unset(request.partner_label_id):
            body['partnerLabelId'] = request.partner_label_id
        if not UtilClient.is_unset(request.partner_num):
            body['partnerNum'] = request.partner_num
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SendInvitationResponse(),
            await self.do_roarequest_async('SendInvitation', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partnerDepartments/invitations/send', 'none', req, runtime)
        )

    def set_dept_partner_type_and_num(
        self,
        request: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumRequest,
    ) -> dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumHeaders()
        return self.set_dept_partner_type_and_num_with_options(request, headers, runtime)

    async def set_dept_partner_type_and_num_async(
        self,
        request: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumRequest,
    ) -> dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumHeaders()
        return await self.set_dept_partner_type_and_num_with_options_async(request, headers, runtime)

    def set_dept_partner_type_and_num_with_options(
        self,
        request: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumRequest,
        headers: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.label_ids):
            body['labelIds'] = request.label_ids
        if not UtilClient.is_unset(request.partner_num):
            body['partnerNum'] = request.partner_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse(),
            self.do_roarequest('SetDeptPartnerTypeAndNum', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partnerDepartments', 'none', req, runtime)
        )

    async def set_dept_partner_type_and_num_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumRequest,
        headers: dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_id):
            body['deptId'] = request.dept_id
        if not UtilClient.is_unset(request.label_ids):
            body['labelIds'] = request.label_ids
        if not UtilClient.is_unset(request.partner_num):
            body['partnerNum'] = request.partner_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.SetDeptPartnerTypeAndNumResponse(),
            await self.do_roarequest_async('SetDeptPartnerTypeAndNum', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/partnerDepartments', 'none', req, runtime)
        )

    def update_file_status(
        self,
        request: dingtalkexclusive__1__0_models.UpdateFileStatusRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateFileStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateFileStatusHeaders()
        return self.update_file_status_with_options(request, headers, runtime)

    async def update_file_status_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateFileStatusRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateFileStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateFileStatusHeaders()
        return await self.update_file_status_with_options_async(request, headers, runtime)

    def update_file_status_with_options(
        self,
        request: dingtalkexclusive__1__0_models.UpdateFileStatusRequest,
        headers: dingtalkexclusive__1__0_models.UpdateFileStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateFileStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_ids):
            body['requestIds'] = request.request_ids
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateFileStatusResponse(),
            self.do_roarequest('UpdateFileStatus', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/sending/files/status', 'json', req, runtime)
        )

    async def update_file_status_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateFileStatusRequest,
        headers: dingtalkexclusive__1__0_models.UpdateFileStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateFileStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.request_ids):
            body['requestIds'] = request.request_ids
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateFileStatusResponse(),
            await self.do_roarequest_async('UpdateFileStatus', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/sending/files/status', 'json', req, runtime)
        )

    def update_mini_app_version_status(
        self,
        request: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusHeaders()
        return self.update_mini_app_version_status_with_options(request, headers, runtime)

    async def update_mini_app_version_status_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusHeaders()
        return await self.update_mini_app_version_status_with_options_async(request, headers, runtime)

    def update_mini_app_version_status_with_options(
        self,
        request: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusRequest,
        headers: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.version_type):
            body['versionType'] = request.version_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse(),
            self.do_roarequest('UpdateMiniAppVersionStatus', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/versionStatus', 'json', req, runtime)
        )

    async def update_mini_app_version_status_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusRequest,
        headers: dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mini_app_id):
            body['miniAppId'] = request.mini_app_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.version_type):
            body['versionType'] = request.version_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateMiniAppVersionStatusResponse(),
            await self.do_roarequest_async('UpdateMiniAppVersionStatus', 'exclusive_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/exclusive/miniApps/versions/versionStatus', 'json', req, runtime)
        )

    def update_partner_visibility(
        self,
        request: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityRequest,
    ) -> dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdatePartnerVisibilityHeaders()
        return self.update_partner_visibility_with_options(request, headers, runtime)

    async def update_partner_visibility_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityRequest,
    ) -> dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdatePartnerVisibilityHeaders()
        return await self.update_partner_visibility_with_options_async(request, headers, runtime)

    def update_partner_visibility_with_options(
        self,
        request: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityRequest,
        headers: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.label_id):
            body['labelId'] = request.label_id
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse(),
            self.do_roarequest('UpdatePartnerVisibility', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/partnerDepartments/visibilityPartners', 'boolean', req, runtime)
        )

    async def update_partner_visibility_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityRequest,
        headers: dingtalkexclusive__1__0_models.UpdatePartnerVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.label_id):
            body['labelId'] = request.label_id
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdatePartnerVisibilityResponse(),
            await self.do_roarequest_async('UpdatePartnerVisibility', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/partnerDepartments/visibilityPartners', 'boolean', req, runtime)
        )

    def update_role_visibility(
        self,
        request: dingtalkexclusive__1__0_models.UpdateRoleVisibilityRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateRoleVisibilityHeaders()
        return self.update_role_visibility_with_options(request, headers, runtime)

    async def update_role_visibility_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateRoleVisibilityRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateRoleVisibilityHeaders()
        return await self.update_role_visibility_with_options_async(request, headers, runtime)

    def update_role_visibility_with_options(
        self,
        request: dingtalkexclusive__1__0_models.UpdateRoleVisibilityRequest,
        headers: dingtalkexclusive__1__0_models.UpdateRoleVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.label_id):
            body['labelId'] = request.label_id
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse(),
            self.do_roarequest('UpdateRoleVisibility', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/partnerDepartments/visibilityRoles', 'boolean', req, runtime)
        )

    async def update_role_visibility_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateRoleVisibilityRequest,
        headers: dingtalkexclusive__1__0_models.UpdateRoleVisibilityHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dept_ids):
            body['deptIds'] = request.dept_ids
        if not UtilClient.is_unset(request.label_id):
            body['labelId'] = request.label_id
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateRoleVisibilityResponse(),
            await self.do_roarequest_async('UpdateRoleVisibility', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/partnerDepartments/visibilityRoles', 'boolean', req, runtime)
        )

    def update_storage_mode(
        self,
        request: dingtalkexclusive__1__0_models.UpdateStorageModeRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateStorageModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateStorageModeHeaders()
        return self.update_storage_mode_with_options(request, headers, runtime)

    async def update_storage_mode_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateStorageModeRequest,
    ) -> dingtalkexclusive__1__0_models.UpdateStorageModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkexclusive__1__0_models.UpdateStorageModeHeaders()
        return await self.update_storage_mode_with_options_async(request, headers, runtime)

    def update_storage_mode_with_options(
        self,
        request: dingtalkexclusive__1__0_models.UpdateStorageModeRequest,
        headers: dingtalkexclusive__1__0_models.UpdateStorageModeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateStorageModeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_storage_mode):
            body['fileStorageMode'] = request.file_storage_mode
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateStorageModeResponse(),
            self.do_roarequest('UpdateStorageMode', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/storageModes', 'json', req, runtime)
        )

    async def update_storage_mode_with_options_async(
        self,
        request: dingtalkexclusive__1__0_models.UpdateStorageModeRequest,
        headers: dingtalkexclusive__1__0_models.UpdateStorageModeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkexclusive__1__0_models.UpdateStorageModeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_storage_mode):
            body['fileStorageMode'] = request.file_storage_mode
        if not UtilClient.is_unset(request.target_corp_id):
            body['targetCorpId'] = request.target_corp_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkexclusive__1__0_models.UpdateStorageModeResponse(),
            await self.do_roarequest_async('UpdateStorageMode', 'exclusive_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/exclusive/fileStorages/acrossClouds/storageModes', 'json', req, runtime)
        )
