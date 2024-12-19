from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class TelegramUser(AbstractUser):
    telegram_id = models.BigIntegerField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="telegramuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="telegramuser_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    