from .celery import app as celery_app

# to load celery when this app starts
# code that will be executed when the celery worker is started
__all__ = ("celery_app",)