from django.contrib.auth.models import AbstractUser
from django.db import models


class TelegramUser(AbstractUser):
    telegram_id = models.BigIntegerField(unique=True)
