from dataclasses import dataclass
from authorization.infrastructure.broker.events.base import BaseEvent


@dataclass
class CreateUserEvent(BaseEvent):
    event_name: str = 'create_user'
    telegram_id: str
    username: str
    first_name: str
    token: str
