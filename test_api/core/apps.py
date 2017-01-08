from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        import core.signals