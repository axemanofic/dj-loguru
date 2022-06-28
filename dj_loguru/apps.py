from django.apps import AppConfig
from django.core.checks import Tags, register

from django_simple_logs.checks import check_settings


class DjangoSimpleLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_simple_logs'

    def ready(self) -> None:
        register(Tags.security)(check_settings)
