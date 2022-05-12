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


class InternalEndpoint(object):

    def __init__(self, esHttpEndpoint=None, esTcpEndpoint=None, kibanaEndpoint=None):
        """
        :param esHttpEndpoint: (Optional) es http endpoint
        :param esTcpEndpoint: (Optional) es tcp endpoint
        :param kibanaEndpoint: (Optional) kibana endpoint
        """

        self.esHttpEndpoint = esHttpEndpoint
        self.esTcpEndpoint = esTcpEndpoint
        self.kibanaEndpoint = kibanaEndpoint
