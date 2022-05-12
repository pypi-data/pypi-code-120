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


class DescribeIpCleanThresholdRangeRequest(JDCloudRequest):
    """
    查询公网 IP 可设置清洗阈值范围, 支持 ipv4 和 ipv6
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIpCleanThresholdRangeRequest, self).__init__(
            '/regions/{regionId}/describeIpCleanThresholdRange', 'GET', header, version)
        self.parameters = parameters


class DescribeIpCleanThresholdRangeParameters(object):

    def __init__(self, regionId, ip):
        """
        :param regionId: 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州
        :param ip: 基础防护已防护公网 IP, 支持 ipv4 和 ipv6. 
<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources'>describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP
<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources'>describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP
<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describewafipresources'>describeWafIpResources</a> 接口查询基础防护已防护的Web应用防火墙 IP
<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeccsipresources'>describeCcsIpResources</a> 接口查询基础防护已防护的托管区公网 IP

        """

        self.regionId = regionId
        self.ip = ip

