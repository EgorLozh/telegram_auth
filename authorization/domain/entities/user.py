from dataclasses import dataclass, field

from authorization.domain.entities.base import BaseEntity
from authorization.domain.repos import BaseUserRepo
from authorization.domain.values.token import UserToken


@dataclass
class User(BaseEntity):
    repo: BaseUserRepo
    token: UserToken = field(default_factory=UserToken)
    first_name: str | None = None
    username: str | None = None
    telegram_id: int | None = None

    def save(self):
        self.repo.save(self)