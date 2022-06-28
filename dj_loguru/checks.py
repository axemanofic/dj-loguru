from typing import List, Any
from django.apps import AppConfig
from django.core.checks import Error
from django_simple_logs.defaults import default_loguru_settings, default_ignore_urls
from django_simple_logs.conf import conf


def check_settings(app_configs: List[AppConfig], **kwargs: Any) -> List[Error]:
    errors = []

    if not isinstance(conf.DJANGO_SIMPLE_LOGS, dict):
        errors.append(
            Error("DJANGO_SIMPLE_LOGS should be a dict.")
        )
    if not isinstance(conf.DJANGO_SIMPLE_LOGS.get("LOGURU", default_loguru_settings), dict):
        errors.append(
            Error("LOGURU should be a dict.")
        )
    if not isinstance(conf.DJANGO_SIMPLE_LOGS.get("IGNORE_URLS", default_ignore_urls), list):
        errors.append(
            Error("IGNORE_URLS should be a list.")
        )
    return errors
