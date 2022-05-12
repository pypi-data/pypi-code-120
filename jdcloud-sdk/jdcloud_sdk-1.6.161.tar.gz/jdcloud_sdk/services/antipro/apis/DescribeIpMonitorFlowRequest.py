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


class DescribeIpMonitorFlowRequest(JDCloudRequest):
    """
    查询公网 IP 的监控流量
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIpMonitorFlowRequest, self).__init__(
            '/describeIpMonitorFlow', 'GET', header, version)
        self.parameters = parameters


class DescribeIpMonitorFlowParameters(object):

    def __init__(self, startTime, endTime, ip):
        """
        :param startTime: 开始时间, 只能查询最近 90 天以内的数据, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        :param endTime: 查询的结束时间, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        :param ip: DDoS 防护包已防护的公网 IP. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-protection-package/api/describeprotectediplist'>describeProtectedIpList</a> 接口查询 DDoS 防护包已防护的公网 IP
        """

        self.startTime = startTime
        self.endTime = endTime
        self.ip = ip

