import os

from paradoxdjango.core.exceptions import ImproperlyConfigured
from paradoxdjango.template import Context
from paradoxdjango.template.engine import Engine
from paradoxdjango.test import SimpleTestCase, override_settings

from .utils import ROOT, TEMPLATE_DIR

OTHER_DIR = os.path.join(ROOT, "other_templates")


class EngineTest(SimpleTestCase):
    def test_repr_empty(self):
        engine = Engine()
        self.assertEqual(
            repr(engine),
            "<Engine: app_dirs=False debug=False loaders=[("
            "'paradoxdjango.template.loaders.cached.Loader', "
            "['paradoxdjango.template.loaders.filesystem.Loader'])] "
            "string_if_invalid='' file_charset='utf-8' builtins=["
            "'paradoxdjango.template.defaulttags', 'paradoxdjango.template.defaultfilters', "
            "'paradoxdjango.template.loader_tags'] autoescape=True>",
        )

    def test_repr(self):
        engine = Engine(
            dirs=[TEMPLATE_DIR],
            context_processors=["paradoxdjango.template.context_processors.debug"],
            debug=True,
            loaders=["paradoxdjango.template.loaders.filesystem.Loader"],
            string_if_invalid="x",
            file_charset="utf-16",
            libraries={"custom": "template_tests.templatetags.custom"},
            autoescape=False,
        )
        self.assertEqual(
            repr(engine),
            f"<Engine: dirs=[{TEMPLATE_DIR!r}] app_dirs=False "
            "context_processors=['paradoxdjango.template.context_processors.debug'] "
            "debug=True loaders=['paradoxdjango.template.loaders.filesystem.Loader'] "
            "string_if_invalid='x' file_charset='utf-16' "
            "libraries={'custom': 'template_tests.templatetags.custom'} "
            "builtins=['paradoxdjango.template.defaulttags', "
            "'paradoxdjango.template.defaultfilters', 'paradoxdjango.template.loader_tags'] "
            "autoescape=False>",
        )


class RenderToStringTest(SimpleTestCase):
    def setUp(self):
        self.engine = Engine(dirs=[TEMPLATE_DIR])

    def test_basic_context(self):
        self.assertEqual(
            self.engine.render_to_string("test_context.html", {"obj": "test"}),
            "obj:test\n",
        )

    def test_autoescape_off(self):
        engine = Engine(dirs=[TEMPLATE_DIR], autoescape=False)
        self.assertEqual(
            engine.render_to_string("test_context.html", {"obj": "<script>"}),
            "obj:<script>\n",
        )


class GetDefaultTests(SimpleTestCase):
    @override_settings(TEMPLATES=[])
    def test_no_engines_configured(self):
        msg = "No DjangoTemplates backend is configured."
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            Engine.get_default()

    @override_settings(
        TEMPLATES=[
            {
                "NAME": "default",
                "BACKEND": "paradoxdjango.template.backends.paradoxdjango.DjangoTemplates",
                "OPTIONS": {"file_charset": "abc"},
            }
        ]
    )
    def test_single_engine_configured(self):
        self.assertEqual(Engine.get_default().file_charset, "abc")

    @override_settings(
        TEMPLATES=[
            {
                "NAME": "default",
                "BACKEND": "paradoxdjango.template.backends.paradoxdjango.DjangoTemplates",
                "OPTIONS": {"file_charset": "abc"},
            },
            {
                "NAME": "other",
                "BACKEND": "paradoxdjango.template.backends.paradoxdjango.DjangoTemplates",
                "OPTIONS": {"file_charset": "def"},
            },
        ]
    )
    def test_multiple_engines_configured(self):
        self.assertEqual(Engine.get_default().file_charset, "abc")


class LoaderTests(SimpleTestCase):
    def test_origin(self):
        engine = Engine(dirs=[TEMPLATE_DIR], debug=True)
        template = engine.get_template("index.html")
        self.assertEqual(template.origin.template_name, "index.html")

    def test_loader_priority(self):
        """
        #21460 -- The order of template loader works.
        """
        loaders = [
            "paradoxdjango.template.loaders.filesystem.Loader",
            "paradoxdjango.template.loaders.app_directories.Loader",
        ]
        engine = Engine(dirs=[OTHER_DIR, TEMPLATE_DIR], loaders=loaders)
        template = engine.get_template("priority/foo.html")
        self.assertEqual(template.render(Context()), "priority\n")

    def test_cached_loader_priority(self):
        """
        The order of template loader works. Refs #21460.
        """
        loaders = [
            (
                "paradoxdjango.template.loaders.cached.Loader",
                [
                    "paradoxdjango.template.loaders.filesystem.Loader",
                    "paradoxdjango.template.loaders.app_directories.Loader",
                ],
            ),
        ]
        engine = Engine(dirs=[OTHER_DIR, TEMPLATE_DIR], loaders=loaders)

        template = engine.get_template("priority/foo.html")
        self.assertEqual(template.render(Context()), "priority\n")

        template = engine.get_template("priority/foo.html")
        self.assertEqual(template.render(Context()), "priority\n")
