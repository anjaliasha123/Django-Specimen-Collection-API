from .base import * #noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-bc9j1ver9!g0mgc4yif2n#=r70#6gle2g)8az87v)hrw=-nagr',
    )

# people who will get email regarding code errors in production
ADMINS= [("Anna", "ajacobash@gmail.com")]

# TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = []

SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS") + ["*"]
ADMIN_URL = env("DJANGO_ADMIN_URL")
DATABASES = {"default": env.db("DATABASE_URL")}
SESSION_COOKIE_SECURE = True

DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="Anna Support roadmaplearner",)

SITE_NAME = "RoadMap Learner"

SERVER_EMAIL= env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[RoadMapLearner]")

# celery email configuration
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "ajacobash@example.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Anna"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}