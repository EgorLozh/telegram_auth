from abc import ABC, abstractmethod

from authorization.application.queries.base import BaseQuery


class BaseQueryHandler(ABC):
    @abstractmethod
    def __call__(self, query: BaseQuery):
        pass
