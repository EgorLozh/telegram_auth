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
        return self.repo.save(self)

    def update(self):
        return self.repo.update(self)

from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.entities.token import UserToken
