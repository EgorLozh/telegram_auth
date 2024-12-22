from abc import ABC, abstractmethod
from typing import Optional

from authorization.domain.filters.base import BaseFilter


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
    def select(self, filter: BaseFilter) -> Optional['UserToken']:
        ...

    @abstractmethod
    def update(self, token: 'UserToken') -> 'UserToken':
        ...
    
    @abstractmethod
    def delete(self, token: 'UserToken') -> 'UserToken':
        ...

from authorization.domain.entities.token import UserToken