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


class GetBrowserCheckSettingRequest(JDCloudRequest):
    """
    浏览器完整性检查与不良行为检查类似，寻找最常被垃圾邮件发送者滥用的常见HTTP头，并拒绝他们访问您的页面。它还会对没有用户代理或非标准用户代理（也是滥用机器人、爬虫或访客常用的）的访客提出挑战质询。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetBrowserCheckSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$browser_check', 'GET', header, version)
        self.parameters = parameters


class GetBrowserCheckSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier

