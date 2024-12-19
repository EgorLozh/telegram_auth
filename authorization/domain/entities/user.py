from dataclasses import dataclass, field

from authorization.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    repo: 'BaseUserRepo'
    token: 'UserToken'
    id: int | None = None
    first_name: str | None = None
    username: str | None = None
    telegram_id: int | None = None

    def save(self):
        self.repo.save(self)

from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.entities.token import UserToken
