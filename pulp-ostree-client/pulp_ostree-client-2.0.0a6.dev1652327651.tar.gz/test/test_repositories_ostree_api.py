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

import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.api.repositories_ostree_api import RepositoriesOstreeApi  # noqa: E501
from pulpcore.client.pulp_ostree.rest import ApiException


class TestRepositoriesOstreeApi(unittest.TestCase):
    """RepositoriesOstreeApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_ostree.api.repositories_ostree_api.RepositoriesOstreeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create an ostree repository  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete an ostree repository  # noqa: E501
        """
        pass

    def test_import_commits(self):
        """Test case for import_commits

        Import commits to a repository  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List ostree repositorys  # noqa: E501
        """
        pass

    def test_modify(self):
        """Test case for modify

        Modify repository  # noqa: E501
        """
        pass

    def test_partial_update(self):
        """Test case for partial_update

        Update an ostree repository  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect an ostree repository  # noqa: E501
        """
        pass

    def test_sync(self):
        """Test case for sync

        Sync from remote  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update an ostree repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
