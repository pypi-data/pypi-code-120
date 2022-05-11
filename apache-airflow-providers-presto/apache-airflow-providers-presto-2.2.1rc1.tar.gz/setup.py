#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE
# OVERWRITTEN WHEN PREPARING PACKAGES.
#
# IF YOU WANT TO MODIFY IT, YOU SHOULD MODIFY THE TEMPLATE
# `SETUP_TEMPLATE.py.jinja2` IN the `dev/provider_packages` DIRECTORY

"""Setup.py for the apache-airflow-providers-presto package."""

from setuptools import find_namespace_packages, setup

version = '2.2.1'


def do_setup():
    """Perform the package apache-airflow-providers-presto setup."""
    setup(
        version=version,
        extras_require={'google': ['apache-airflow-providers-google']},
        packages=find_namespace_packages(include=['airflow.providers.presto', 'airflow.providers.presto.*']),
    )


if __name__ == "__main__":
    do_setup()
