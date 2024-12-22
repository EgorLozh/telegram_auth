from django.db import models

from authorization.infrastructure.models.user import TelegramUser


class UserToken(models.Model):
    telegram_user = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, null=True, blank=True, related_name="token")
    expired_at = models.DateTimeField()
    token = models.CharField(max_length=255, unique=True)
