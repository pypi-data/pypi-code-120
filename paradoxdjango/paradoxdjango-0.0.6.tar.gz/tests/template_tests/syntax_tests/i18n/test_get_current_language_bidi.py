from template_tests.utils import setup

from paradoxdjango.template import TemplateSyntaxError
from paradoxdjango.test import SimpleTestCase


class I18nGetCurrentLanguageBidiTagTests(SimpleTestCase):
    libraries = {"i18n": "paradoxdjango.templatetags.i18n"}

    @setup({"template": "{% load i18n %} {% get_current_language_bidi %}"})
    def test_no_as_var(self):
        msg = (
            "'get_current_language_bidi' requires 'as variable' (got "
            "['get_current_language_bidi'])"
        )
        with self.assertRaisesMessage(TemplateSyntaxError, msg):
            self.engine.render_to_string("template")
