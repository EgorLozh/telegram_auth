from abc import ABC, abstractmethod

from events.base import BaseEvent


class BaseHandler(ABC):
    @abstractmethod
    async def __call__(self, event: BaseEvent):
        ...
