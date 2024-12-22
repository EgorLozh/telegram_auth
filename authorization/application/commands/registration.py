from dataclasses import dataclass

from django.http.request import HttpRequest
from authorization.application.commands.base import BaseCommand


@dataclass
class RegistrationCommand(BaseCommand):
    request: HttpRequest
