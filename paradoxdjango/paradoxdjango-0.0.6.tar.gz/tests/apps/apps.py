from paradoxdjango.apps import AppConfig


class MyAdmin(AppConfig):
    name = "paradoxdjango.contrib.admin"
    verbose_name = "Admin sweet admin."


class MyAuth(AppConfig):
    name = "paradoxdjango.contrib.auth"
    label = "myauth"
    verbose_name = "All your password are belong to us."


class BadConfig(AppConfig):
    """This class doesn't supply the mandatory 'name' attribute."""


class NotAConfig:
    name = "apps"


class NoSuchApp(AppConfig):
    name = "there is no such app"


class PlainAppsConfig(AppConfig):
    name = "apps"


class RelabeledAppsConfig(AppConfig):
    name = "apps"
    label = "relabeled"


class ModelPKAppsConfig(AppConfig):
    name = "apps"
    default_auto_field = "paradoxdjango.db.models.BigAutoField"
