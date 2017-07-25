from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "bao"

    def ready(self):
        import_module("bao.receivers")
