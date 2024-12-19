from dataclasses import dataclass

from rest_framework.request import Request

from authorization.application.commands.base import BaseCommand


@dataclass
class LogoutCommand(BaseCommand):
    request: Request

