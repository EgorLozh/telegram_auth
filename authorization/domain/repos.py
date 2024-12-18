from abc import ABC, abstractmethod


class BaseUserRepo(ABC):
    @abstractmethod
    def save(self, user: 'User') -> 'User':
        ...

class BaseUserTokenRepo(ABC):
    @abstractmethod
    def save(self, token: 'Token', user: 'User' = None) -> 'Token':
        ...

from authorization.domain.entities.user import User
from contextvars import Token