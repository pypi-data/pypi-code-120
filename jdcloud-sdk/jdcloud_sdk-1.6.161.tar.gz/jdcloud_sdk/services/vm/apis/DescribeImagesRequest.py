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


class DescribeImagesRequest(JDCloudRequest):
    """
    
查询镜像信息列表。

详细操作说明请参考帮助文档：[镜像概述](https://docs.jdcloud.com/cn/virtual-machines/image-overview)

## 接口说明
- 通过此接口可以查询到京东云官方镜像、第三方镜像、镜像市场、私有镜像、或其他用户共享给您的镜像。
- 请求参数即过滤条件，每个条件之间的关系为逻辑与（AND）的关系。
- 如果使用子帐号查询，只会查询到该子帐号有权限的镜像。关于资源权限请参考 [IAM概述](https://docs.jdcloud.com/cn/iam/product-overview)。
- 单次查询最大可查询100条镜像信息。
- 尽量一次调用接口查询多条数据，不建议使用该批量查询接口一次查询一条数据，如果使用不当导致查询过于密集，可能导致网关触发限流。
- 由于该接口为 `GET` 方式请求，最终参数会转换为 `URL` 上的参数，但是 `HTTP` 协议下的 `GET` 请求参数长度是有大小限制的，使用者需要注意参数超长的问题。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeImagesRequest, self).__init__(
            '/regions/{regionId}/images', 'GET', header, version)
        self.parameters = parameters


class DescribeImagesParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域ID。
        """

        self.regionId = regionId
        self.imageSource = None
        self.offline = None
        self.platform = None
        self.ids = None
        self.imageName = None
        self.rootDeviceType = None
        self.launchPermission = None
        self.status = None
        self.serviceCode = None
        self.architecture = None
        self.pageNumber = None
        self.pageSize = None

    def setImageSource(self, imageSource):
        """
        :param imageSource: (Optional) 镜像来源，如果没有指定 `ids` 参数，此参数必传。取值范围：
`public`：官方镜像。
`thirdparty`：镜像市场镜像。
`private`：用户自己的私有镜像。
`shared`：其他用户分享的镜像。
`community`：社区镜像。

        """
        self.imageSource = imageSource

    def setOffline(self, offline):
        """
        :param offline: (Optional) 查询已经下线的镜像时使用。
只有查询 `官方镜像` 或者 `镜像市场镜像` 时，此参数才有意义，其它情况下此参数无效。
指定 `ids` 查询时，此参数无效。

        """
        self.offline = offline

    def setPlatform(self, platform):
        """
        :param platform: (Optional) 根据镜像的操作系统发行版查询。
取值范围：`Ubuntu、CentOS、Windows Server`。

        """
        self.platform = platform

    def setIds(self, ids):
        """
        :param ids: (Optional) 指定镜像ID查询，如果指定了此参数，其它参数可以不传。

        """
        self.ids = ids

    def setImageName(self, imageName):
        """
        :param imageName: (Optional) 根据镜像名称模糊查询。
        """
        self.imageName = imageName

    def setRootDeviceType(self, rootDeviceType):
        """
        :param rootDeviceType: (Optional) 根据镜像支持的系统盘类型查询。支持范围：`localDisk` 本地系统盘镜像；`cloudDisk` 云盘系统盘镜像。
        """
        self.rootDeviceType = rootDeviceType

    def setLaunchPermission(self, launchPermission):
        """
        :param launchPermission: (Optional) 根据镜像的使用权限查询，可选参数，仅当 `imageSource` 为 `private` 时有效。取值范围：
`all`：没有限制，所有人均可以使用。
`specifiedUsers`：只有共享用户可以使用。
`ownerOnly`：镜像拥有者自己可以使用。

        """
        self.launchPermission = launchPermission

    def setStatus(self, status):
        """
        :param status: (Optional) 根据镜像状态查询。参考 [镜像状态](https://docs.jdcloud.com/virtual-machines/api/image_status)
        """
        self.status = status

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 已废弃。
        """
        self.serviceCode = serviceCode

    def setArchitecture(self, architecture):
        """
        :param architecture: (Optional) CPU架构。支持范围：`x86_64`、`aarch64`。
        """
        self.architecture = architecture

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；<br>默认为20；取值范围[10, 100]。
        """
        self.pageSize = pageSize

