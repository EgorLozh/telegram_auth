from abc import ABC, abstractmethod
from dataclasses import dataclass

from authorization.infrastructure.broker.events.base import BaseEvent


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, event: BaseEvent):
        ...
