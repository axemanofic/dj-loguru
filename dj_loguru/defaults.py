import sys

from django.conf import settings
from typing import Dict, List

default_loguru_settings: Dict = {
    "handlers": [
        {
            "sink": sys.stdout,
            "filter": lambda record: record['level'].name == 'INFO',
            "format": '{time} | {level} | {message}',
        },
        {
            "sink": settings.BASE_DIR / 'logs/error.log',
            "filter": lambda record: record['level'].name == 'ERROR',
            "format": '{time} | {level} | {message}',
            "rotation": '100 KB',
            "compression": 'zip',
        }
    ]
}

default_ignore_urls: List = [
        "silk",
        "swagger",
        "redoc",
        "admin",
        "media"
]
