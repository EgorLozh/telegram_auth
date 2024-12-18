from abc import ABC, abstractmethod


class BaseUserRepo(ABC):
    from authorization.domain.entities.user import User
    
    @abstractmethod
    def save(self, user: 'User') -> 'User':
        ...

class BaseUserTokenRepo(ABC): 
    from authorization.domain.entities.user import User
    from contextvars import Token
    @abstractmethod
    def save(self, token: 'Token', user: 'User' = None) -> 'Token':
        ...
