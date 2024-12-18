from django.db import models

from authorization.infrastructure.models.user import TelegramUser


class UserToken(models.Model):
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=255, unique=True)
