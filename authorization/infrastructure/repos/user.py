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
        return self.to_entity(model)

    def update(self, user):
        model = TelegramUser.objects.get(id=user.id)
        model.telegram_id = user.telegram_id
        model.first_name = user.first_name
        model.username = user.username
        model.save()
        return self.to_entity(model)
    
    def select(self, filter: ByUserId) -> UserTokenEntity | None:
        model = TelegramUser.objects.filter(**filter.get_filter_dict()).first()
        if model:
            return self.to_entity(model)
        return None

    def to_model(self, user: User):
        return TelegramUser(id=user.id,
                            telegram_id=user.telegram_id,
                            first_name=user.first_name,
                            username=user.username)
    
    def to_entity(self, model: TelegramUser, transfer_token=None):
        from authorization.infrastructure.repos.user_token import UserTokenRepo
        token_repo = UserTokenRepo()
        if not transfer_token:
            token = token_repo.select(ByUserId(id=model.pk))
        else:
            token = transfer_token
        return User(id=model.pk,
                    repo=self,
                    token=token,
                    first_name=model.first_name,
                    username=model.username,
                    telegram_id=model.telegram_id)
                    
        