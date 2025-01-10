from .base import * #noqa
from .base import env
# TODO: CHANGE SECRET KEY
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-bc9j1ver9!g0mgc4yif2n#=r70#6gle2g)8az87v)hrw=-nagr',
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# list of origings allowed. since we are using nginx, we add its domain
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

# celery email configuration
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "ajacobash@example.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Anna"