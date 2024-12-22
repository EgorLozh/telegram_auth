from dataclasses import dataclass
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import ValidationError

from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.commands.login import LoginCommand
from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.filters.user import ByTelegramToken


@dataclass
class LoginCommandHandler(BaseCommandHandler):
    user_repo: BaseUserRepo
    def __call__(self, command: LoginCommand):
        
        user = self.user_repo.select(ByTelegramToken(token=command.telegram_token))
        if not user:
            raise ValidationError({"error": "Неверное имя пользователя или пароль."})
        
        login(command.request, self.user_repo.to_model(user))
