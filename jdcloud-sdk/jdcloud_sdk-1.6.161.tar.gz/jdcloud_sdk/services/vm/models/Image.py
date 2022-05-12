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


class Image(object):

    def __init__(self, imageId=None, name=None, platform=None, osVersion=None, architecture=None, systemDiskSizeGB=None, imageSource=None, osType=None, status=None, createTime=None, sizeMB=None, desc=None, ownerPin=None, launchPermission=None, systemDisk=None, dataDisks=None, snapshotId=None, rootDeviceType=None, progress=None, offline=None, serviceCode=None, imported=None):
        """
        :param imageId: (Optional) 镜像ID。
        :param name: (Optional) 镜像名称。
        :param platform: (Optional) 镜像的操作系统平台名称。
取值范围：`Ubuntu、CentOS、Windows Server、Other Linux、Other Windows`。

        :param osVersion: (Optional) 镜像的操作系统版本。
        :param architecture: (Optional) 镜像架构。取值范围：`x86_64、i386`。
        :param systemDiskSizeGB: (Optional) 镜像系统盘大小。
        :param imageSource: (Optional) 镜像来源，取值范围：
`public`：官方镜像。
`thirdparty`：镜像市场镜像。
`private`：用户自己的私有镜像。
`shared`：其他用户分享的镜像。
`community`：社区镜像。

        :param osType: (Optional) 镜像的操作系统类型。取值范围：`windows、linux`。
        :param status: (Optional) 镜像状态。参考 [镜像状态](https://docs.jdcloud.com/virtual-machines/api/image_status)。
        :param createTime: (Optional) 镜像的创建时间。
        :param sizeMB: (Optional) 镜像文件的实际大小。
        :param desc: (Optional) 镜像描述。
        :param ownerPin: (Optional) 该镜像拥有者的用户PIN。
        :param launchPermission: (Optional) 镜像的使用权限。取值范围：
`all`：没有限制，所有人均可以使用。
`specifiedUsers`：只有共享用户可以使用。
`ownerOnly`：镜像拥有者自己可以使用。

        :param systemDisk: (Optional) 镜像系统盘配置。
        :param dataDisks: (Optional) 镜像数据盘配置列表。
        :param snapshotId: (Optional) 创建云盘系统盘所使用的快照ID。系统盘类型为本地盘的镜像，此参数为空。
        :param rootDeviceType: (Optional) 镜像支持的系统盘类型。取值范围：
`localDisk`：本地盘系统盘。
`cloudDisk`：云盘系统盘。

        :param progress: (Optional) 镜像复制和转换时的进度，仅显示数值，单位为百分比。
        :param offline: (Optional) 镜像的上下线状态。`offline=true` 的镜像不再允许创建云主机。
        :param serviceCode: (Optional) 已废弃。
        :param imported: (Optional) 是否来自导入镜像。
        """

        self.imageId = imageId
        self.name = name
        self.platform = platform
        self.osVersion = osVersion
        self.architecture = architecture
        self.systemDiskSizeGB = systemDiskSizeGB
        self.imageSource = imageSource
        self.osType = osType
        self.status = status
        self.createTime = createTime
        self.sizeMB = sizeMB
        self.desc = desc
        self.ownerPin = ownerPin
        self.launchPermission = launchPermission
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.snapshotId = snapshotId
        self.rootDeviceType = rootDeviceType
        self.progress = progress
        self.offline = offline
        self.serviceCode = serviceCode
        self.imported = imported
