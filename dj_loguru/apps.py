from django.apps import AppConfig
from django.core.checks import Tags, register

from dj_loguru.checks import check_settings


class DjangoSimpleLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj_loguru'

    def ready(self) -> None:
        register(Tags.security)(check_settings)
