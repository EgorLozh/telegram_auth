from datetime import datetime
import pytz
from authorization.domain.entities.user import User
from authorization.domain.filters.token import ByTokenOid, ByUserId
from authorization.domain.filters.user import ByUsername
from authorization.infrastructure.broker.event_handlers.base import BaseEventHandler
from authorization.infrastructure.broker.events.create_user_event import CreateUserEvent
from authorization.infrastructure.repos.user import UserRepo
from authorization.infrastructure.repos.user_token import UserTokenRepo


class CreateUserEventHandler(BaseEventHandler):
    user_repo: UserRepo = UserRepo()
    user_token_repo: UserTokenRepo = UserTokenRepo()
    def __call__(self, event: CreateUserEvent):
        token = self.user_token_repo.select(ByTokenOid(oid=event.token))
        if not token or token.expired_at < datetime.now(pytz.UTC):
            return None
        user = User(repo=self.user_repo, 
                    token=token, 
                    telegram_id=event.telegram_id, 
                    username=event.username, 
                    first_name=event.first_name)
        if not self.user_repo.select(ByUsername(username=user.username)):
            user = user.save()
        else:
            user = self.user_repo.select(ByUsername(username=user.username))
        token.user = user
        old_token = self.user_token_repo.select(ByUserId(id=user.id))
        if old_token:
            self.user_token_repo.delete(old_token)
        token.update()
        
        return user
