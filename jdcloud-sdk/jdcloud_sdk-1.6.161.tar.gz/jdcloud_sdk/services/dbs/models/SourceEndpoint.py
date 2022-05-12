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


class SourceEndpoint(object):

    def __init__(self, networkType, port, backupAgentId, accountName, password, engineRelatedConfig, ):
        """
        :param networkType:  源数据库的网络类型 PublicAccess 和 RDS
        :param port:  源数据库的端口
        :param backupAgentId:  备份代理的ID，仅初始化时可设置，设置完成并开始备份后，不可修改
        :param accountName:  源数据库的账号
        :param password:  源数据库的密码
        :param engineRelatedConfig:  不同数据库引擎独有的配置参数
        """

        self.networkType = networkType
        self.port = port
        self.backupAgentId = backupAgentId
        self.accountName = accountName
        self.password = password
        self.engineRelatedConfig = engineRelatedConfig
