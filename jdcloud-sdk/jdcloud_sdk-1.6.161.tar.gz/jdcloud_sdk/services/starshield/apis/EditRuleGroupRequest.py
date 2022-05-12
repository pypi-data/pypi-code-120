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


class EditRuleGroupRequest(JDCloudRequest):
    """
    更新规则组的状态
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(EditRuleGroupRequest, self).__init__(
            '/zones/{zone_identifier}/firewall$$waf$$packages/{package_identifier}/groups/{identifier}', 'PATCH', header, version)
        self.parameters = parameters


class EditRuleGroupParameters(object):

    def __init__(self, zone_identifier, package_identifier, identifier, ):
        """
        :param zone_identifier: 
        :param package_identifier: 
        :param identifier: 
        """

        self.zone_identifier = zone_identifier
        self.package_identifier = package_identifier
        self.identifier = identifier
        self.mode = None

    def setMode(self, mode):
        """
        :param mode: (Optional) 该组中包含的规则是否可配置/可使用
        """
        self.mode = mode

