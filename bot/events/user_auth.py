from aiogram.types import Message

from dataclasses import dataclass
from events.base import BaseEvent

@dataclass
class UserAuthEvent(BaseEvent):
    message: Message
    token: str
