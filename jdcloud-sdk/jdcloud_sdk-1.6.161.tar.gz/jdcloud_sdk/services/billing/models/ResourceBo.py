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


class ResourceBo(object):

    def __init__(self, pin=None, appCode=None, appCodeName=None, serviceCode=None, serviceCodeName=None, region=None, resourceId=None, formula=None, billingType=None, status=None, startTime=None, endTime=None):
        """
        :param pin: (Optional) pin
        :param appCode: (Optional) 应用码code
        :param appCodeName: (Optional) 应用码名称
        :param serviceCode: (Optional) 服务码code
        :param serviceCodeName: (Optional) 服务码名称
        :param region: (Optional) 资源所属地域
        :param resourceId: (Optional) 资源id
        :param formula: (Optional) 资源配置
        :param billingType: (Optional) 计费类型 1、按配置，2、按用量，3、包年包月，4、按次
        :param status: (Optional) 资源状态：1、正常，2、停服
        :param startTime: (Optional) 计费开始时间
        :param endTime: (Optional) 计费结束时间
        """

        self.pin = pin
        self.appCode = appCode
        self.appCodeName = appCodeName
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.region = region
        self.resourceId = resourceId
        self.formula = formula
        self.billingType = billingType
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
