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


class SetOnlineBillingTypeRequest(JDCloudRequest):
    """
    设置线上计费方式
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetOnlineBillingTypeRequest, self).__init__(
            '/onlineBillingType', 'POST', header, version)
        self.parameters = parameters


class SetOnlineBillingTypeParameters(object):

    def __init__(self, ):
        """
        """

        self.allType = None

    def setAllType(self, allType):
        """
        :param allType: (Optional) 计费方式,取值[0,1],0:日流量计费,1:日峰值带宽计费.
        """
        self.allType = allType

