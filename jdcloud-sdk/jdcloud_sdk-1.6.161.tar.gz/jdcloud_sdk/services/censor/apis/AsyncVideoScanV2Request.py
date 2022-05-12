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


class AsyncVideoScanV2Request(JDCloudRequest):
    """
    提交视频异步检测任务V2
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AsyncVideoScanV2Request, self).__init__(
            '/video:asyncscanv2', 'POST', header, version)
        self.parameters = parameters


class AsyncVideoScanV2Parameters(object):

    def __init__(self, ):
        """
        """

        self.bizType = None
        self.url = None
        self.dataId = None
        self.version = None
        self.title = None
        self.callback = None
        self.callbackUrl = None
        self.uniqueKey = None
        self.scFrequency = None
        self.advancedFrequency = None

    def setBizType(self, bizType):
        """
        :param bizType: (Optional) 业务bizType，请联系客户经理获取
        """
        self.bizType = bizType

    def setUrl(self, url):
        """
        :param url: (Optional) 最大长度512, 点播视频地址
        """
        self.url = url

    def setDataId(self, dataId):
        """
        :param dataId: (Optional) 最大长度128，点播视频唯一标识
        """
        self.dataId = dataId

    def setVersion(self, version):
        """
        :param version: (Optional) 接口版本号，可选值 v3.2
        """
        self.version = version

    def setTitle(self, title):
        """
        :param title: (Optional) 最大长度512，视频名称
        """
        self.title = title

    def setCallback(self, callback):
        """
        :param callback: (Optional) 最大长度512，数据回调参数，产品根据业务情况自行设计，当获取离线检测结果时，内容安全服务会返回该字段
        """
        self.callback = callback

    def setCallbackUrl(self, callbackUrl):
        """
        :param callbackUrl: (Optional) 最大长度256，离线结果回调通知到客户的URL。主动回调数据接口超时时间设置为2s，为了保证顺利接收数据，需保证接收接口性能稳定并且保证幂等性。
        """
        self.callbackUrl = callbackUrl

    def setUniqueKey(self, uniqueKey):
        """
        :param uniqueKey: (Optional) 最大长度64，客户个性化视频唯一性标识，传入后，将以此值作为重复检测依据，若不传，默认以URL作为查重依据,如果重复提交会被拒绝，返回报错信息请求重复，以及原提交taskID值，具体返回请查看响应示例
        """
        self.uniqueKey = uniqueKey

    def setScFrequency(self, scFrequency):
        """
        :param scFrequency: (Optional) 最大长度64，客户个性化视频唯一性标识，传入后，将以此值作为重复检测依据，若不传，默认以URL作为查重依据,如果重复提交会被拒绝，返回报错信息请求重复，以及原提交taskID值，具体返回请查看响应示例
        """
        self.scFrequency = scFrequency

    def setAdvancedFrequency(self, advancedFrequency):
        """
        :param advancedFrequency: (Optional) 高级截帧设置，此项填写，默认截帧策略失效
        """
        self.advancedFrequency = advancedFrequency

