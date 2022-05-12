# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeIpv6GatewayRequest(JDCloudRequest):
    """
    查询IPv6网关实例详情
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIpv6GatewayRequest, self).__init__(
            '/regions/{regionId}/ipv6Gateways/{ipv6GatewayId}', 'GET', header, version)
        self.parameters = parameters


class DescribeIpv6GatewayParameters(object):

    def __init__(self, regionId, ipv6GatewayId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegions）获取云物理服务器支持的地域
        :param ipv6GatewayId: IPv6网关ID
        """

        self.regionId = regionId
        self.ipv6GatewayId = ipv6GatewayId

