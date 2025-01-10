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