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


class NodeGroup(object):

    def __init__(self, clusterId=None, nodeGroupId=None, name=None, description=None, nodeConfig=None, version=None, nodeNetwork=None, currentCount=None, expectCount=None, agId=None, azs=None, instanceTemplateId=None, state=None, tags=None, updateTime=None, stateMessage=None, autoRepair=None, progress=None, caConfig=None, createdTime=None):
        """
        :param clusterId: (Optional) 集群 id
        :param nodeGroupId: (Optional) 工作节点组 id
        :param name: (Optional) 工作节点组名称
        :param description: (Optional) 工作节点组描述
        :param nodeConfig: (Optional) 工作节点组配置信息
        :param version: (Optional) 工作节点版本
        :param nodeNetwork: (Optional) 工作节点所属的网络信息
        :param currentCount: (Optional) 当前工作节点数量
        :param expectCount: (Optional) 期望的工作节点数量
        :param agId: (Optional) 工作节点组的ag id ，通过agid可以查询该工作节点组下的实例
        :param azs: (Optional) 工作节点组所在的 az
        :param instanceTemplateId: (Optional) 工作节点组的 ag 对应的实例模板
        :param state: (Optional) 状态  [pending,running,resizing,reconciling,deleting,deleted,error,running_with_error(部分节点有问题)]
        :param tags: (Optional) 
        :param updateTime: (Optional) 更新时间
        :param stateMessage: (Optional) 状态变更原因
        :param autoRepair: (Optional) 是否开启自动修复
        :param progress: (Optional) 控制节点操作进度
        :param caConfig: (Optional) 自动伸缩配置
        :param createdTime: (Optional) 创建时间
        """

        self.clusterId = clusterId
        self.nodeGroupId = nodeGroupId
        self.name = name
        self.description = description
        self.nodeConfig = nodeConfig
        self.version = version
        self.nodeNetwork = nodeNetwork
        self.currentCount = currentCount
        self.expectCount = expectCount
        self.agId = agId
        self.azs = azs
        self.instanceTemplateId = instanceTemplateId
        self.state = state
        self.tags = tags
        self.updateTime = updateTime
        self.stateMessage = stateMessage
        self.autoRepair = autoRepair
        self.progress = progress
        self.caConfig = caConfig
        self.createdTime = createdTime
