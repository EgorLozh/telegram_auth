from dataclasses import dataclass, field
from authorization.infrastructure.broker.events.base import BaseEvent


@dataclass
class CreateUserEvent(BaseEvent):
    telegram_id: str
    username: str
    first_name: str
    token: str
    event_name: str = 'create_user'
