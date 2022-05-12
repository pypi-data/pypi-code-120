import copy
import unittest

from paradoxdjango.db import DEFAULT_DB_ALIAS, connection, connections
from paradoxdjango.test import SimpleTestCase


@unittest.skipUnless(connection.vendor == "sqlite", "SQLite tests")
class TestDbSignatureTests(SimpleTestCase):
    def test_custom_test_name(self):
        test_connection = copy.copy(connections[DEFAULT_DB_ALIAS])
        test_connection.settings_dict = copy.deepcopy(
            connections[DEFAULT_DB_ALIAS].settings_dict
        )
        test_connection.settings_dict["NAME"] = None
        test_connection.settings_dict["TEST"]["NAME"] = "custom.sqlite.db"
        signature = test_connection.creation_class(test_connection).test_db_signature()
        self.assertEqual(signature, (None, "custom.sqlite.db"))

    def test_get_test_db_clone_settings_name(self):
        test_connection = copy.copy(connections[DEFAULT_DB_ALIAS])
        test_connection.settings_dict = copy.deepcopy(
            connections[DEFAULT_DB_ALIAS].settings_dict,
        )
        tests = [
            ("test.sqlite3", "test_1.sqlite3"),
            ("test", "test_1"),
        ]
        for test_db_name, expected_clone_name in tests:
            with self.subTest(test_db_name=test_db_name):
                test_connection.settings_dict["NAME"] = test_db_name
                test_connection.settings_dict["TEST"]["NAME"] = test_db_name
                creation_class = test_connection.creation_class(test_connection)
                clone_settings_dict = creation_class.get_test_db_clone_settings("1")
                self.assertEqual(clone_settings_dict["NAME"], expected_clone_name)
