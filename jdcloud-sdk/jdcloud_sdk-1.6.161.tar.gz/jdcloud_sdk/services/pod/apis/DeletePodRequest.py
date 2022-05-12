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


class DeletePodRequest(JDCloudRequest):
    """
    pod 状态必须为 stopped、running 或 error状态。 <br>
按量付费的实例，如不主动删除将一直运行，不再使用的实例，可通过本接口主动停用。<br>
只能支持主动删除按量计费类型的实例。包年包月过期的 pod 也可以删除，其它的情况还请发工单系统。计费状态异常的容器无法删除。
 [MFA enabled]
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeletePodRequest, self).__init__(
            '/regions/{regionId}/pods/{podId}', 'DELETE', header, version)
        self.parameters = parameters


class DeletePodParameters(object):

    def __init__(self, regionId, podId, ):
        """
        :param regionId: Region ID
        :param podId: Pod ID
        """

        self.regionId = regionId
        self.podId = podId

