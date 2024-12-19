from dataclasses import dataclass
from django.shortcuts import redirect
from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.commands.registration import RegistrationCommand
from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.domain.entities.token import UserToken
from configs.settings import Settings


@dataclass
class RegistrationCommandHandler(BaseCommandHandler):
    settings: Settings
    token_repo: BaseUserTokenRepo
    def __call__(self, command: RegistrationCommand):
        token = UserToken(repo=self.token_repo)
        token.save()
        url = self.settings.BOT_URL + '?start=' + token.oid
        return redirect(url)


