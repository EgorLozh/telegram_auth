from dataclasses import dataclass
from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.entities.token import UserToken
from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.domain.entities.user import User
from authorization.domain.filters.base import BaseFilter
from authorization.domain.filters.user import ByUserId
from authorization.infrastructure.models.user_tokens import UserToken as UserTokenModel



class UserTokenRepo(BaseUserTokenRepo):

    def save(self, token: 'UserToken') -> 'UserToken':
        model = self.to_model(token)
        model.save()
        return self.to_entity(model)
    
    def delete(self, token: 'UserToken') -> 'UserToken':
        model = UserTokenModel.objects.get(token=token.oid)
        model.delete()
        return self.to_entity(model)
    
    def update(self, token: 'UserToken') -> 'UserToken':
        from authorization.infrastructure.repos.user import UserRepo
        user_repo = UserRepo()
        model = UserTokenModel.objects.get(token=token.oid)
        model.expired_at = token.expired_at
        model.token = token.oid
        model.telegram_user = user_repo.to_model(token.user)
        model.save()
        return self.to_entity(model)
    
    def to_model(self, token: UserToken) -> UserTokenModel:
        from authorization.infrastructure.repos.user import UserRepo
        user_repo = UserRepo()
        user_model = None
        if token.user:
            user_model = user_repo.select(ByUserId(id=token.user.id))
        return UserTokenModel(token=token.oid, 
                              expired_at=token.expired_at, 
                              telegram_user=user_model)
    
    def to_entity(self, model: UserTokenModel) -> UserToken:
        from authorization.infrastructure.repos.user import UserRepo
        user_repo = UserRepo()

        user_token = UserToken(oid=model.token, 
                         repo = self,
                         expired_at=model.expired_at)
        if model.telegram_user:
            user = user_repo.to_entity(model.telegram_user, transfer_token=user_token)
            user_token.user = user
        return  user_token
    
    def select(self, filter: BaseFilter) -> UserToken | None:
        model = UserTokenModel.objects.filter(**filter.get_filter_dict()).first()
        if model:
            return self.to_entity(model)
        return None