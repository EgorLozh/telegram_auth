from abc import ABC, abstractmethod



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

from authorization.domain.entities.user import User
