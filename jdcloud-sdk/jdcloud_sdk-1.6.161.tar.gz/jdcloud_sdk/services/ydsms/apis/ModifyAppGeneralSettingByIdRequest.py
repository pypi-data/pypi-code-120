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


class ModifyAppGeneralSettingByIdRequest(JDCloudRequest):
    """
    修改应用通用设置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyAppGeneralSettingByIdRequest, self).__init__(
            '/smsAppGeneralSettings/{id}:modify', 'GET', header, version)
        self.parameters = parameters


class ModifyAppGeneralSettingByIdParameters(object):

    def __init__(self, , ):
        """
        """

        self.id = None
        self.settingValue = None
        self.status = None

    def setId(self, id):
        """
        :param id: (Optional) id
        """
        self.id = id

    def setSettingValue(self, settingValue):
        """
        :param settingValue: (Optional) 设置的值
        """
        self.settingValue = settingValue

    def setStatus(self, status):
        """
        :param status: (Optional) 是否启用，当前设置是否生效，0未生效 1生效
        """
        self.status = status

