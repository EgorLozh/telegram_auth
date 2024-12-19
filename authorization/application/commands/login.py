from dataclasses import dataclass

from rest_framework.request import Request

from authorization.application.commands.base import BaseCommand


@dataclass
class LoginCommand(BaseCommand):
    request: Request
    username: str
    password: str
