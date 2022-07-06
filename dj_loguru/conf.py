from django.conf import settings
from typing import Union
from dj_loguru.defaults import default_loguru_settings, default_ignore_urls


class Settings:
    @property
    def DJANGO_SIMPLE_LOGS(self):
        return getattr(settings, "DJANGO_LOGURU", default_loguru_settings)


conf = Settings()
