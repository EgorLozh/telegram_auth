from dataclasses import dataclass, field
import pytz

from datetime import datetime, timedelta
from typing import Optional
import uuid



TOKEN_LIVE_TIME = timedelta(minutes=5)

@dataclass
class UserToken:

    repo: 'BaseUserTokenRepo'
    oid: str = field(default_factory=lambda: str(uuid.uuid4()))
    expired_at: datetime = field(default_factory=lambda: datetime.now(pytz.UTC) + TOKEN_LIVE_TIME)
    user: Optional['User'] = None

    
    def save(self):
        self.repo.save(self)

    def update(self):
        self.repo.update(self)

from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.domain.entities.user import User
    