# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

"""
blueapps.conf
=============
"""

import os
import importlib


def get_config_module():
    config_path = os.getenv("BK_APP_CONFIG_PATH")
    return importlib.import_module(config_path if config_path else "config")


def get_config_default_module():
    config_path = os.getenv("BK_APP_CONFIG_PATH")
    return importlib.import_module("%s.default" % config_path if config_path else "config.default")


def get_settings_from_module(module, is_upper=True):
    setting_items = {}
    for _setting in dir(module):
        if is_upper and not _setting.isupper():
            continue
        setting_items[_setting] = getattr(module, _setting)
    return setting_items


class BlueSettings(object):
    def __init__(self):
        from django.conf import settings as django_settings
        from blueapps.conf import default_settings

        self._django_settings = django_settings
        self._default_settings = default_settings

    def __getattr__(self, key):
        if key == key.upper():
            if hasattr(self._django_settings, key):
                return getattr(self._django_settings, key)
            elif hasattr(self._default_settings, key):
                return getattr(self._default_settings, key)

        raise AttributeError(
            "%r object has no attribute %r" % (self.__class__.__name__, key)
        )


settings = BlueSettings()
