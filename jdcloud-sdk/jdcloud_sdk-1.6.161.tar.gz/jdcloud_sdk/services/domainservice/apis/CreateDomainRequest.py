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


class CreateDomainRequest(JDCloudRequest):
    """
    添加主域名  
如何添加免费域名，详细情况请查阅<a href="https://docs.jdcloud.com/cn/jd-cloud-dns/domainadd">文档</a>
添加收费域名，请查阅<a href="https://docs.jdcloud.com/cn/jd-cloud-dns/purchase-process">文档</a>，
添加收费域名前，请确保用户的京东云账户有足够的资金支付，Openapi接口回返回订单号，可以用此订单号向计费系统查阅详情。

    """

    def __init__(self, parameters, header=None, version="v2"):
        super(CreateDomainRequest, self).__init__(
            '/regions/{regionId}/domain', 'POST', header, version)
        self.parameters = parameters


class CreateDomainParameters(object):

    def __init__(self, regionId, packId, domainName, ):
        """
        :param regionId: 实例所属的地域ID
        :param packId: 主域名的套餐类型, 免费:0 企业版:1 企业高级版:2
        :param domainName: 要添加的主域名
        """

        self.regionId = regionId
        self.packId = packId
        self.domainName = domainName
        self.domainId = None
        self.buyType = None
        self.timeSpan = None
        self.timeUnit = None
        self.billingType = None

    def setDomainId(self, domainId):
        """
        :param domainId: (Optional) 主域名的ID，升级套餐必填，请使用describeDomains获取
        """
        self.domainId = domainId

    def setBuyType(self, buyType):
        """
        :param buyType: (Optional) 新购买:1、升级:3，收费套餐的域名必填
        """
        self.buyType = buyType

    def setTimeSpan(self, timeSpan):
        """
        :param timeSpan: (Optional) 取值1，2，3 ，含义：时长，收费套餐的域名必填
        """
        self.timeSpan = timeSpan

    def setTimeUnit(self, timeUnit):
        """
        :param timeUnit: (Optional) 时间单位，收费套餐的域名必填，1：小时，2：天，3：月，4：年
        """
        self.timeUnit = timeUnit

    def setBillingType(self, billingType):
        """
        :param billingType: (Optional) 计费类型，可以不传此参数。
        """
        self.billingType = billingType

