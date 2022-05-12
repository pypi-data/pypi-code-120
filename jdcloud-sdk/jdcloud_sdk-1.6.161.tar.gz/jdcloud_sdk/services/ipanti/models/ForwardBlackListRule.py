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


class ForwardBlackListRule(object):

    def __init__(self, status=None, ipSetId=None, ipSetName=None, ip=None):
        """
        :param status: (Optional) 是否开启, 0: 关闭, 1: 开启
        :param ipSetId: (Optional) 引用的 IP 黑白名单 Id
        :param ipSetName: (Optional) 引用的 IP 黑白名单名称
        :param ip: (Optional) 为 IP 或 IP 段的数组
        """

        self.status = status
        self.ipSetId = ipSetId
        self.ipSetName = ipSetName
        self.ip = ip
