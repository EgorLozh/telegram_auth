from dataclasses import dataclass
from django.contrib.auth import logout

from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.commands.logout import LogoutCommand


@dataclass
class LogoutCommandHandler(BaseCommandHandler):
    def __call__(self, command: LogoutCommand):
        logout(command.request)
        