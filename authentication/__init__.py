from django.apps import AppConfig

class AuthenticationAppConfig(AppConfig):
    name = 'register.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import register.apps.authentication.signals

default_app_config = 'register.apps.authentication.AuthenticationAppConfig'