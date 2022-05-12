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


class ComStamp(object):

    def __init__(self, stampMax=None, signPositionType=None, keyword=None, positionX=None, positionY=None, offsetX=None, offsetY=None, page=None, sealName=None, imageB64=None, stampId=None, desc=None, isDefault=None, imageType=None, imageSize=None, imageHeight=None, imageWidth=None, orgName=None, legalPersonName=None, transactorName=None, transactorIdCardNum=None, transactorMobile=None, identifyType=None, identifyValue=None):
        """
        :param stampMax: (Optional) 最多盖章数目（默认10）
        :param signPositionType: (Optional) 盖章类型（0 坐标 1 关键字 默认1 ）
        :param keyword: (Optional) 盖章关键字（与坐标二选一）
        :param positionX: (Optional) 盖章X坐标（与关键字二选一）
        :param positionY: (Optional) 盖章Y坐标（与关键字二选一）
        :param offsetX: (Optional) 盖章X坐标偏移量（配合positionX）
        :param offsetY: (Optional) 盖章Y坐标偏移量（配合positionY）
        :param page: (Optional) 盖章页码（选择坐标盖章时需要）
        :param sealName: (Optional) 印章名称
        :param imageB64: (Optional) 印章图像base64(建议png格式,不传使用默认圆形章)
        :param stampId: (Optional) 印章ID
        :param desc: (Optional) 印章描述
        :param isDefault: (Optional) 是否作为以后签章默认章
        :param imageType: (Optional) 图片类型，只支持png格式
        :param imageSize: (Optional) 图片大小，高度*宽度
        :param imageHeight: (Optional) 图片高度
        :param imageWidth: (Optional) 图片宽度
        :param orgName: (Optional) 公司名称
        :param legalPersonName: (Optional) 法人姓名
        :param transactorName: (Optional) 代办人姓名
        :param transactorIdCardNum: (Optional) 代办人身份证号码
        :param transactorMobile: (Optional) 代办人手机号
        :param identifyType: (Optional) 标记字段 - usci(统一社会信用码) orgCode（组织机构代码） businessNum （工商营业执照号）
        :param identifyValue: (Optional) 标记值
        """

        self.stampMax = stampMax
        self.signPositionType = signPositionType
        self.keyword = keyword
        self.positionX = positionX
        self.positionY = positionY
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.page = page
        self.sealName = sealName
        self.imageB64 = imageB64
        self.stampId = stampId
        self.desc = desc
        self.isDefault = isDefault
        self.imageType = imageType
        self.imageSize = imageSize
        self.imageHeight = imageHeight
        self.imageWidth = imageWidth
        self.orgName = orgName
        self.legalPersonName = legalPersonName
        self.transactorName = transactorName
        self.transactorIdCardNum = transactorIdCardNum
        self.transactorMobile = transactorMobile
        self.identifyType = identifyType
        self.identifyValue = identifyValue
