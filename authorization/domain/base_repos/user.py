from abc import ABC, abstractmethod
from typing import Optional

from authorization.domain.filters.base import BaseFilter



class BaseUserRepo(ABC):
    
    @abstractmethod
    def save(self, user: 'User') -> 'User':
        ...

    @abstractmethod
    def to_model(self, user: 'User'):
        ...

    @abstractmethod
    def to_entity(self, model):
        ...

    @abstractmethod
    def select(self, filter: BaseFilter) -> Optional['User']:
        ...

    @abstractmethod
    def update(self, user: 'User') -> 'User':
        ...

from authorization.domain.entities.user import User
