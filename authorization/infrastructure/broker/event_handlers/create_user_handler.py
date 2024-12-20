from datetime import datetime
from authorization.domain.entities.user import User
from authorization.domain.filters.token import ByTokenOid
from authorization.infrastructure.broker.event_handlers.base import BaseEventHandler
from authorization.infrastructure.broker.events.create_user_event import CreateUserEvent
from authorization.infrastructure.repos.user import UserRepo
from authorization.infrastructure.repos.user_token import UserTokenRepo


class CreateUserEventHandler(BaseEventHandler):
    user_repo: UserRepo
    user_token_repo: UserTokenRepo
    def __call__(self, event: CreateUserEvent):
        token = self.user_token_repo.select(ByTokenOid(oid=event.token))
        if not token or token.expired_at > datetime.now():
            return None
        user = User(repo=self.user_repo, 
                    token=token, 
                    telegram_id=event.telegram_id, 
                    username=event.username, 
                    first_name=event.first_name)
        user.save()
        return user