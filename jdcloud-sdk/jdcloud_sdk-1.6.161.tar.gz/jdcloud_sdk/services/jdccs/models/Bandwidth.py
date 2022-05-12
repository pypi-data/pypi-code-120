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


class Bandwidth(object):

    def __init__(self, idc=None, idcName=None, bandwidthId=None, bandwidthName=None, status=None, lineType=None, chargeType=None, bandwidth=None, relatedIp=None, switchboard=None):
        """
        :param idc: (Optional) 机房英文标识
        :param idcName: (Optional) 机房名称
        :param bandwidthId: (Optional) 带宽实例ID
        :param bandwidthName: (Optional) 带宽名称
        :param status: (Optional) 状态 normal:正常 abnormal:异常
        :param lineType: (Optional) 线路类型 dynamicBGP:动态BGP thirdLineBGP:三线BGP telecom:电信单线 unicom:联通单线 mobile:移动单线
        :param chargeType: (Optional) 计费方式
fixedBandwidth:固定带宽
95thPercentile:95峰值（IN，OUT统一计算95）
merge95thPercentile:95峰值（多出口合并计费）
95thPercentileSeparate:95峰值（IN，OUT分别计算95，取较大者）
merge95thPercentileAvg:日95峰值月平均（多出口合并计费）

        :param bandwidth: (Optional) 合同带宽（Mbps）
        :param relatedIp: (Optional) 关联的公网IP
        :param switchboard: (Optional) 交换机信息
        """

        self.idc = idc
        self.idcName = idcName
        self.bandwidthId = bandwidthId
        self.bandwidthName = bandwidthName
        self.status = status
        self.lineType = lineType
        self.chargeType = chargeType
        self.bandwidth = bandwidth
        self.relatedIp = relatedIp
        self.switchboard = switchboard
