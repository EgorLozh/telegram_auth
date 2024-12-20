from abc import ABC
from dataclasses import dataclass


@dataclass
class BaseEvent(ABC):
    event_name: str
