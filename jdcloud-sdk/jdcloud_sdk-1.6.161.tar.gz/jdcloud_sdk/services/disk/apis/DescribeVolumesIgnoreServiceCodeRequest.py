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


class DescribeVolumesIgnoreServiceCodeRequest(JDCloudRequest):
    """
    -   查询您已经创建的云硬盘。
-   filters多个过滤条件之间是逻辑与(AND)，每个条件内部的多个取值是逻辑或(OR)

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeVolumesIgnoreServiceCodeRequest, self).__init__(
            '/regions/{regionId}/disks:ignoreServiceCode', 'POST', header, version)
        self.parameters = parameters


class DescribeVolumesIgnoreServiceCodeParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.tags = None
        self.filterGroups = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setTags(self, tags):
        """
        :param tags: (Optional) Tag筛选条件
        """
        self.tags = tags

    def setFilterGroups(self, filterGroups):
        """
        :param filterGroups: (Optional) diskId - 云硬盘ID，精确匹配，支持多个
diskType - 云硬盘类型，精确匹配，支持多个，取值为 ssd,premium-hdd,ssd.io1,ssd.gp1,hdd.std1
instanceId - 云硬盘所挂载主机的ID，精确匹配，支持多个
instanceType - 云硬盘所挂载主机的类型，精确匹配，支持多个
status - 可用区，精确匹配，支持多个
az - 云硬盘状态，精确匹配，支持多个
name - 云硬盘名称，模糊匹配，支持单个
multiAttach - 云硬盘是否多点挂载，精确匹配，支持单个
encrypted - 云硬盘是否加密，精确匹配，支持单个
policyId - 绑定policyId的云硬盘，精确匹配，支持多个
notPolicyId - 未绑定policyId的云硬盘，精确匹配，支持多个

        """
        self.filterGroups = filterGroups

