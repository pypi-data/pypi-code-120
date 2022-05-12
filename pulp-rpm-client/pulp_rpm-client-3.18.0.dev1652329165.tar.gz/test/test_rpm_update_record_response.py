# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.rpm_update_record_response import RpmUpdateRecordResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestRpmUpdateRecordResponse(unittest.TestCase):
    """RpmUpdateRecordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RpmUpdateRecordResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.rpm_update_record_response.RpmUpdateRecordResponse()  # noqa: E501
        if include_optional :
            return RpmUpdateRecordResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '0', 
                updated_date = '0', 
                description = '0', 
                issued_date = '0', 
                fromstr = '0', 
                status = '0', 
                title = '0', 
                summary = '0', 
                version = '0', 
                type = '0', 
                severity = '0', 
                solution = '0', 
                release = '0', 
                rights = '0', 
                pushcount = '0', 
                pkglist = [
                    pulpcore.client.pulp_rpm.models.rpm/update_collection_response.rpm.UpdateCollectionResponse(
                        name = '0', 
                        shortname = '0', 
                        module = pulpcore.client.pulp_rpm.models.module.module(), 
                        packages = [
                            None
                            ], )
                    ], 
                references = [
                    None
                    ], 
                reboot_suggested = True
            )
        else :
            return RpmUpdateRecordResponse(
        )

    def testRpmUpdateRecordResponse(self):
        """Test RpmUpdateRecordResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
