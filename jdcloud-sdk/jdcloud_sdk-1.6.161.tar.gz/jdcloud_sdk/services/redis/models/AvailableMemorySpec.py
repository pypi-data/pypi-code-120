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


class AvailableMemorySpec(object):

    def __init__(self, memoryGB=None, soldOut=None, availableZones=None, availableFlavors=None):
        """
        :param memoryGB: (Optional) 售卖内存（GB）
        :param soldOut: (Optional) 是否售罄
        :param availableZones: (Optional) 可用区列表
        :param availableFlavors: (Optional) 规格列表
        """

        self.memoryGB = memoryGB
        self.soldOut = soldOut
        self.availableZones = availableZones
        self.availableFlavors = availableFlavors
