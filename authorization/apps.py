from django.apps import AppConfig


class AuthorizationConfig(AppConfig):    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authorization'

    def ready(self):
        from authorization.infrastructure.models.user import TelegramUser
        from authorization.infrastructure.models.user_tokens import UserToken
