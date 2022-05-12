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


class BlockDetail(object):

    def __init__(self, politics=None, terrorism=None, porn=None, illegal=None, insult=None, ad=None, politics_terrorism=None):
        """
        :param politics: (Optional) 涉政
        :param terrorism: (Optional) 涉恐
        :param porn: (Optional) 涉黄
        :param illegal: (Optional) 违禁
        :param insult: (Optional) 辱骂
        :param ad: (Optional) 广告
        :param politics_terrorism: (Optional) 涉政暴恐
        """

        self.politics = politics
        self.terrorism = terrorism
        self.porn = porn
        self.illegal = illegal
        self.insult = insult
        self.ad = ad
        self.politics_terrorism = politics_terrorism
