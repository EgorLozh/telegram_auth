from dataclasses import dataclass
from datetime import datetime

from authorization.domain.entities.user import User
from authorization.domain.entities.token import UserToken
from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.commands.telegram_user import CreateTelegramUserCommand
from authorization.domain.filters.token import ByTokenOid


@dataclass
class CreateTelegramUserCommandHandler(BaseCommandHandler):
    user_repo: BaseUserRepo
    user_token_repo: BaseUserTokenRepo
    def __call__(self, command: CreateTelegramUserCommand):
        token = self.user_token_repo.select(ByTokenOid(oid=command.token))
        if not token or token.expired_at > datetime.now():
            return None
        user = User(repo=self.user_repo, 
                    token=token, 
                    telegram_id=command.telegram_id, 
                    username=command.username, 
                    first_name=command.first_name)
        user.save()
        return user
