from unittest import mock, skipUnless

from paradoxdjango.db import OperationalError, connection
from paradoxdjango.test import TestCase


@skipUnless(connection.vendor == "sqlite", "SQLite tests.")
class FeaturesTests(TestCase):
    def test_supports_json_field_operational_error(self):
        if hasattr(connection.features, "supports_json_field"):
            del connection.features.supports_json_field
        msg = "unable to open database file"
        with mock.patch(
            "paradoxdjango.db.backends.base.base.BaseDatabaseWrapper.cursor",
            side_effect=OperationalError(msg),
        ):
            with self.assertRaisesMessage(OperationalError, msg):
                connection.features.supports_json_field
