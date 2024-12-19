from dataclasses import dataclass

from authorization.application.commands.base import BaseCommand
from authorization.domain.entities.token import UserToken


@dataclass
class RegistrationCommand(BaseCommand):
    ...
