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


class BatchOfflineRequest(JDCloudRequest):
    """
    批量下线
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(BatchOfflineRequest, self).__init__(
            '/regions/{regionId}/apiGroups/{apiGroupId}/deployments:offline', 'POST', header, version)
        self.parameters = parameters


class BatchOfflineParameters(object):

    def __init__(self, regionId, apiGroupId, ):
        """
        :param regionId: 地域ID
        :param apiGroupId: 分组ID
        """

        self.regionId = regionId
        self.apiGroupId = apiGroupId
        self.deploymentIds = None

    def setDeploymentIds(self, deploymentIds):
        """
        :param deploymentIds: (Optional) 要删除的部署ID集合，以,分隔
        """
        self.deploymentIds = deploymentIds

