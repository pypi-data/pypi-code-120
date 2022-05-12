from paradoxdjango.db.models.base import ModelState, ModelStateFieldsCacheDescriptor
from paradoxdjango.test import SimpleTestCase


class ModelStateTests(SimpleTestCase):
    def test_fields_cache_descriptor(self):
        self.assertIsInstance(ModelState.fields_cache, ModelStateFieldsCacheDescriptor)
