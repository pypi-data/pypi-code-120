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


class CallDataDetail(object):

    def __init__(self, ip=None, addr=None, eid=None, phone=None, pin=None, card=None):
        """
        :param ip: (Optional) IP
        :param addr: (Optional) 地址
        :param eid: (Optional) 设备
        :param phone: (Optional) 手机
        :param pin: (Optional) 账号
        :param card: (Optional) 身份
        """

        self.ip = ip
        self.addr = addr
        self.eid = eid
        self.phone = phone
        self.pin = pin
        self.card = card
