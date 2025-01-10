from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    about_me = models.TextField(
        verbose_name=_("about me"), default="say something about yourself"
    )
    country = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="USA",
        blank=False,
        null=False,
    )
    city = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="Champaign",
        blank=False,
        null=False,
    )
    
    def __str__(self):
        return f"{self.user.first_name}'s Profile"
