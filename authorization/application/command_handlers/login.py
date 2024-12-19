from django.contrib.auth import authenticate, login
from rest_framework.exceptions import ValidationError

from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.commands.login import LoginCommand


class LoginCommandHandler(BaseCommandHandler):
    def __call__(self, command: LoginCommand):
        user = authenticate(command.request, username=command.username, password=command.password)
        if not user:
            raise ValidationError({"error": "Неверное имя пользователя или пароль."})
        
        login(command.request, user)

        return command.request.session.session_key