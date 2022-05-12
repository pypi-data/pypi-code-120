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


class DescribeInstanceTemplatesCustomdataRequest(JDCloudRequest):
    """
    
查询实例模板上的自定义元数据。

详细操作说明请参考帮助文档：[实例模板](https://docs.jdcloud.com/cn/virtual-machines/instance-template-overview)

## 接口说明
- 一般情况下由于自定义元数据比较大，所以限制每次最多查询10个实例模板。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstanceTemplatesCustomdataRequest, self).__init__(
            '/regions/{regionId}/instanceTemplatesCustomData', 'GET', header, version)
        self.parameters = parameters


class DescribeInstanceTemplatesCustomdataParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域ID。
        """

        self.regionId = regionId
        self.filters = None

    def setFilters(self, filters):
        """
        :param filters: (Optional) <b>filters 中支持使用以下关键字进行过滤</b>
`instanceTemplateId`: 实例模板ID，精确匹配，最多支持10个

        """
        self.filters = filters

