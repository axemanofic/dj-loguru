from django.conf import settings
from typing import Union
from django_simple_logs.defaults import default_loguru_settings, default_ignore_urls


class Settings:
    @property
    def DJANGO_SIMPLE_LOGS(self):
        return getattr(settings, "DJANGO_SIMPLE_LOGS", default_loguru_settings)


conf = Settings()
