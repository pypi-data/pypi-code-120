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


class WafQueryAttackDetailsRequest(JDCloudRequest):
    """
    查询攻击记录详情
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(WafQueryAttackDetailsRequest, self).__init__(
            '/wafAttackDetails', 'POST', header, version)
        self.parameters = parameters


class WafQueryAttackDetailsParameters(object):

    def __init__(self, ):
        """
        """

        self.startTime = None
        self.endTime = None
        self.domain = None
        self.sortField = None
        self.sortRule = None
        self.pageNumber = None
        self.pageSize = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.endTime = endTime

    def setDomain(self, domain):
        """
        :param domain: (Optional) 需要查询的域名, 必须为用户pin下有权限的域名
        """
        self.domain = domain

    def setSortField(self, sortField):
        """
        :param sortField: (Optional) 排序字段
        """
        self.sortField = sortField

    def setSortRule(self, sortRule):
        """
        :param sortRule: (Optional) 排序规则：desc，asc
        """
        self.sortRule = sortRule

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码，从1开始
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页大小，默认20
        """
        self.pageSize = pageSize

