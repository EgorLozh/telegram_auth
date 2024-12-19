from functools import lru_cache
from punq import Container, Scope

from authorization.application.command_handlers.registration import RegistrationCommandHandler
from authorization.application.commands.registration import RegistrationCommand
from authorization.application.mediator import Mediator
from authorization.domain.base_repos.user import BaseUserRepo
from authorization.domain.base_repos.user_token import BaseUserTokenRepo
from authorization.infrastructure.repos.user import UserRepo
from authorization.infrastructure.repos.user_token import UserTokenRepo
from configs.settings import Settings


@lru_cache(1)
def get_container() -> Container:
    return _init_container()

def _init_container() -> Container:
    container = Container()

    container.register(Settings, instance=Settings(), scope=Scope.singleton)

    container.register(BaseUserRepo, UserRepo)
    container.register(BaseUserTokenRepo, UserTokenRepo)

    container.register(RegistrationCommandHandler)

    container.register(Mediator, instance=_init_mediator(container), scope=Scope.singleton)

    return container

def _init_mediator(container: Container) -> Mediator:
    mediator = Mediator()
    mediator.register_command(RegistrationCommand, container.resolve(RegistrationCommandHandler))
    return mediator
