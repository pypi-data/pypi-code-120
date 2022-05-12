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


class CreateRDSInstance(object):

    def __init__(self, payType, engine, engineVersion, instanceClass, storageGB, vpcId, subnetId, id=None, name=None, azs=None, status=None, instanceType=None, cloudID=None, createTime=None):
        """
        :param id: (Optional) RDS实例ID
        :param name: (Optional) RDS实例名称
        :param payType:  计费信息,prepaid\postpaid
        :param azs: (Optional) 可用区ID
        :param engine:  实例引擎类型
        :param status: (Optional) 实例状态
        :param instanceType: (Optional) 实例类型
        :param cloudID: (Optional) 所属云提供商ID
        :param engineVersion:  数据库版本号
        :param instanceClass:  实例规格
        :param storageGB:  磁盘大小，单位GB
        :param vpcId:  VPC ID
        :param subnetId:  子网ID
        :param createTime: (Optional) 创建时间
        """

        self.id = id
        self.name = name
        self.payType = payType
        self.azs = azs
        self.engine = engine
        self.status = status
        self.instanceType = instanceType
        self.cloudID = cloudID
        self.engineVersion = engineVersion
        self.instanceClass = instanceClass
        self.storageGB = storageGB
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.createTime = createTime
