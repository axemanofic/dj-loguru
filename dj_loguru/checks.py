from typing import List, Any
from django.apps import AppConfig
from django.core.checks import Error
from dj_loguru.conf import conf
from dj_loguru.defaults import default_loguru_settings, default_ignore_urls


def check_settings(app_configs: List[AppConfig], **kwargs: Any) -> List[Error]:
    errors = []

    if not isinstance(conf.DJANGO_LOGURU, dict):
        errors.append(
            Error("DJANGO_LOGURU should be a dict.")
        )
    if not isinstance(conf.DJANGO_LOGURU.get("LOGURU_CONFIG", default_loguru_settings), dict):
        errors.append(
            Error("LOGURU_CONFIG should be a dict.")
        )
    if not isinstance(conf.DJANGO_LOGURU.get("IGNORE_URLS", default_ignore_urls), list):
        errors.append(
            Error("IGNORE_URLS should be a list.")
        )
    return errors
