from abc import ABC, abstractmethod

from authorization.application.commands.base import BaseCommand


class BaseCommandHandler(ABC):
    @abstractmethod
    def __call__(self, command: BaseCommand):
        pass
