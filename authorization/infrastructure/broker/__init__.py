from functools import lru_cache
from authorization.infrastructure.broker.event_handlers.create_user_handler import CreateUserEventHandler
from authorization.infrastructure.broker.events.create_user_event import CreateUserEvent
from .mediator import Mediator


@lru_cache(1)
def init_mediator() -> Mediator:
    mediator = Mediator()

    mediator.register_handler(CreateUserEvent, CreateUserEventHandler())
    
    mediator.register_event_type(CreateUserEvent.event_name, CreateUserEvent)


init_mediator()
