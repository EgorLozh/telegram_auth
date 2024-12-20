from typing import Dict, Type

from authorization.infrastructure.broker.event_handlers.base import BaseEventHandler
from authorization.infrastructure.broker.events.base import BaseEvent


class Mediator:
    handlers: Dict[Type[BaseEvent], BaseEventHandler] = {}
    event_types: Dict[str, Type[BaseEvent]] = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def register_handler(self, event_type: Type[BaseEvent], handler: BaseEventHandler) -> None:
        self.handlers[event_type] = handler

    def register_event_type(self, event_name: str, event_type: Type[BaseEvent]) -> None:
        self.event_types[event_name] = event_type

    def handle_event(self, event: BaseEvent) -> None:
        if type(event) in self.handlers:
            handler = self.handlers[type(event)]
            return handler(event)

        raise Exception(f'Handler for event {type(event)} not registered')
    
    def get_event_type(self, event_name: str) -> Type[BaseEvent]:
        if event_name in self.event_types:
            return self.event_types[event_name]

        raise Exception(f'Event type {event_name} not registered')
