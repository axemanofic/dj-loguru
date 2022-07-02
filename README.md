# dj-loguru

Simple logging application

## Disclaimer

> I know there is a module https://pypi.org/project/django-loguru/ and it might be a good fit for you. 
> But I decided to make my own module for learning "Middleware".

## Features

* Middleware for logging exceptions
* Decorator for logging exceptions

## Contents
* [How install?](#how-install) 
* [How to work with it?](#how-to-work-with-it) 
* [Set up a django app](#set-up-a-django-app) 
* [How to use @report_bug?](#how-to-use-report_bug)
  * [A Simple Example](#a-simple-example)
* [Have questions?](#have-questions)


## How install?

[Poetry](https://python-poetry.org/)

```sh
poetry add git+https://github.com/axemanofic/dj-loguru.git
```

or [PIP](https://pip.pypa.io/)

```sh
pip install git+https://github.com/axemanofic/dj-loguru.git
```

## Set up a django app

In ``settings.py`` add the following:

```python
MIDDLEWARE = [
    ...
    'dj_loguru.middlewares.LoguruMiddleware',
    ...
]

INSTALLED_APPS = [
    ...
    'dj_loguru',
]
```

Now add the following settings:

```python
DJANGO_LOGURU = {
    "LOGURU_CONFIG": {
        "handlers": [
            {
                "sink": sys.stdout,
                "filter": lambda record: record['level'].name == 'INFO',
                "format": '{time} | {level} | {message}',
            },
            {
                "sink": BASE_DIR / 'logs/error.log',
                "filter": lambda record: record['level'].name == 'ERROR',
                "format": '{time} | {level} | {message}',
                "rotation": '100 KB',
                "compression": 'zip',
            }
        ]
    },
    "IGNORE_URLS": [
        "silk",
        "swagger",
        "redoc",
        "admin",
        "media"
    ]
}
```

### LOGURU_CONFIG

Use this loguru config, or read their [documentation for your own customization](https://github.com/Delgan/loguru#suitable-for-scripts-and-libraries)

### IGNORE_URLS

Some urls don't return JSON format, so you need to add those keywords of your url to an array. 
The example shows the default urls:
* media (localhost:8000/media/)
* silk (localhost:8000/silk/)
* etc...

## Have questions?

If you have questions then "welcome" to my [telegram](https://t.me/axemanofic) 