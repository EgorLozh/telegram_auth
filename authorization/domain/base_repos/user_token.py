from abc import ABC, abstractmethod
from typing import Optional


class BaseUserTokenRepo(ABC):

    @abstractmethod
    def save(self, token: 'UserToken') -> 'UserToken':
        ...

    @abstractmethod
    def to_model(self, token: 'UserToken'):
        ...

    @abstractmethod
    def to_entity(self, model):
        ...

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Optional['UserToken']:
        ...

from authorization.domain.entities.token import UserToken