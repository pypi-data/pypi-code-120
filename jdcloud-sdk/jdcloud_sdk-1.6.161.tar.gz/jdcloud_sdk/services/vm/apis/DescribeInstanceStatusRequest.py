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


class DescribeInstanceStatusRequest(JDCloudRequest):
    """
    
查询一台或多台云主机实例的状态。

云主机实例的状态说明请参考帮助文档：[云主机状态](https://docs.jdcloud.com/cn/virtual-machines/api/vm_status)

## 接口说明
- 使用 `filters` 过滤器进行条件筛选，每个 `filter` 之间的关系为逻辑与（AND）的关系。
- 单次查询最大可查询100条云主机状态。
- 尽量一次调用接口查询多条数据，不建议使用该批量查询接口一次查询一条数据，如果使用不当导致查询过于密集，可能导致网关触发限流。
- 由于该接口为 `GET` 方式请求，最终参数会转换为 `URL` 上的参数，但是 `HTTP` 协议下的 `GET` 请求参数长度是有大小限制的，使用者需要注意参数超长的问题。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstanceStatusRequest, self).__init__(
            '/regions/{regionId}/instanceStatus', 'GET', header, version)
        self.parameters = parameters


class DescribeInstanceStatusParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域ID。
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；<br>默认为20；取值范围[10, 100]。
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) <b>filters 中支持使用以下关键字进行过滤</b>
`instanceId`: 云主机ID，精确匹配，支持多个
`privateIpAddress`: 主网卡内网主IP地址，模糊匹配，支持多个
`vpcId`: 私有网络ID，精确匹配，支持多个
`status`: 云主机状态，精确匹配，支持多个，参考 [云主机状态](https://docs.jdcloud.com/virtual-machines/api/vm_status)
`name`: 云主机名称，模糊匹配，支持单个
`imageId`: 镜像ID，精确匹配，支持多个
`agId`: 使用可用组id，支持单个
`faultDomain`: 错误域，支持多个
`networkInterfaceId`: 弹性网卡ID，精确匹配，支持多个
`subnetId`: 子网ID，精确匹配，支持多个

        """
        self.filters = filters

