from authorization.domain.entities.token import UserToken
from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.infrastructure.models.user_tokens import UserToken as UserTokenModel


class UserTokenRepo(BaseUserTokenRepo):
    def save(self, token: 'UserToken') -> 'UserToken':
        model = self.to_model(token)
        model.save()
        return token
    
    def to_model(self, token: UserToken) -> UserTokenModel:
        from authorization.infrastructure.repos.user import UserRepo
        user_repo = UserRepo()
        user_model = None
        if token.user:
            user_model = user_repo.to_model(token.user)
        return UserTokenModel(token=token.oid, 
                              expired_at=token.expired_at, 
                              telegram_user=user_model)
    
    def to_entity(self, model: UserTokenModel) -> UserToken:
        from authorization.infrastructure.repos.user import UserRepo
        user_repo = UserRepo()
        user = None
        if model.telegram_user:
            user = user_repo.to_entity(model.telegram_user)
        return UserToken(oid=model.token, 
                         expired_at=model.expired_at, 
                         user=user)
    
    def get_by_user_id(self, user_id: int) -> UserToken | None:
        model = UserTokenModel.objects.filter(telegram_user__pk=user_id).first()
        if model:
            return self.to_entity(model)
        return None