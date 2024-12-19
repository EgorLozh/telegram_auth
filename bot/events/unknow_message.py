from dataclasses import dataclass
from aiogram.types import Message

from events.base import BaseEvent


@dataclass
class UnknownMessageEvent(BaseEvent):
    message: Message
