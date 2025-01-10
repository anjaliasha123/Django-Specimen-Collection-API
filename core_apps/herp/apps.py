from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HerpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.herp'
    verbose_name = _("Herp")
