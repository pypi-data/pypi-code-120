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


class ParamInfo(object):

    def __init__(self, description=None, isMulti=None, name=None, optional=None, paramType=None, required=None, valueType=None):
        """
        :param description: (Optional) 描述
        :param isMulti: (Optional) 是否多值,默认为false
        :param name: (Optional) 名称
        :param optional: (Optional) 可选值
        :param paramType: (Optional) 参数类型，目前只有datasource
        :param required: (Optional) 是否必须
        :param valueType: (Optional) 值类型，int, float, string
        """

        self.description = description
        self.isMulti = isMulti
        self.name = name
        self.optional = optional
        self.paramType = paramType
        self.required = required
        self.valueType = valueType
