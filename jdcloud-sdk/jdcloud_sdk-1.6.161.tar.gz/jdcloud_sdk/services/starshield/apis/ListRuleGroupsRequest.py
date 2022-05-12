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


class ListRuleGroupsRequest(JDCloudRequest):
    """
    搜索、列出和排序包中包含的规则组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ListRuleGroupsRequest, self).__init__(
            '/zones/{zone_identifier}/firewall$$waf$$packages/{package_identifier}/groups', 'GET', header, version)
        self.parameters = parameters


class ListRuleGroupsParameters(object):

    def __init__(self, zone_identifier, package_identifier, ):
        """
        :param zone_identifier: 
        :param package_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.package_identifier = package_identifier
        self.name = None
        self.mode = None
        self.rules_count = None
        self.page = None
        self.per_page = None
        self.order = None
        self.direction = None
        self.match = None

    def setName(self, name):
        """
        :param name: (Optional) 防火墙规则组名称
        """
        self.name = name

    def setMode(self, mode):
        """
        :param mode: (Optional) 此组中包含的规则是否可配置/可用
        """
        self.mode = mode

    def setRules_count(self, rules_count):
        """
        :param rules_count: (Optional) 此组中包含多少条规则
        """
        self.rules_count = rules_count

    def setPage(self, page):
        """
        :param page: (Optional) 分页结果的页码
        """
        self.page = page

    def setPer_page(self, per_page):
        """
        :param per_page: (Optional) 每页的组数
        """
        self.per_page = per_page

    def setOrder(self, order):
        """
        :param order: (Optional) 按字段对组进行排序
        """
        self.order = order

    def setDirection(self, direction):
        """
        :param direction: (Optional) asc-升序；desc-降序
        """
        self.direction = direction

    def setMatch(self, match):
        """
        :param match: (Optional) 是否匹配所有搜索要求或至少一个（任何）
        """
        self.match = match

