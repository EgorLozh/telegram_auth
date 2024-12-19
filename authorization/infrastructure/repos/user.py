from authorization.domain.filters.token import ByUserId
from authorization.infrastructure.models.user import TelegramUser
from authorization.infrastructure.models.user_tokens import UserToken as UserTokenModel
from authorization.domain.entities.user import User
from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.entities.token import UserToken as UserTokenEntity


class UserRepo(BaseUserRepo):
    def save(self, user: User) -> None:
        model = self.to_model(user)
        model.save()
    
    def to_model(self, user: User):
        return TelegramUser(pk=user.id,
                            telegram_id=user.telegram_id,
                            first_name=user.first_name,
                            username=user.username)
    
    def to_entity(self, model: TelegramUser):
        from authorization.infrastructure.repos.user_token import UserTokenRepo
        token_repo = UserTokenRepo()
        token = token_repo.select(ByUserId(id=model.pk))
        return User(id=model.pk,
                    repo=self,
                    token=token,
                    first_name=model.first_name,
                    username=model.username,
                    telegram_id=model.telegram_id)
                    
        