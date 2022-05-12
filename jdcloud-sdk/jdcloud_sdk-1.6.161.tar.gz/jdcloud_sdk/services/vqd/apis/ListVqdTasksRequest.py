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


class ListVqdTasksRequest(JDCloudRequest):
    """
    查询视频质检任务列表
支持过滤查询：
  - createTime,ge 最早任务创建时间
  - createTime,le 最晚任务创建时间
  - status,in 任务状态

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ListVqdTasksRequest, self).__init__(
            '/vqdTasks', 'GET', header, version)
        self.parameters = parameters


class ListVqdTasksParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认值为 1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认值为 10；取值范围 [10, 100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 
        """
        self.filters = filters

