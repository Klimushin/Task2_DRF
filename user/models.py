from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name= "user name",
        related_name="profile",
    )

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"