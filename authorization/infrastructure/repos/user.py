from django.db.utils import Q

from authorization.infrastructure.models.user import TelegramUser
from authorization.domain.entities.user import User
from authorization.domain.repos import BaseUserRepo
from authorization.domain.values.token import UserToken


class UserRepo(BaseUserRepo):
    def save(self, user: User) -> None:
        ...
        