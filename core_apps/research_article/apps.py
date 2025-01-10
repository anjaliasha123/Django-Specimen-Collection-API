from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ResearchArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.research_article'
    verbose_name = _("Research Article")

    def ready(self):
        import core_apps.search.signals
