from typing import Dict, Type
from events.base import BaseEvent
from handlers.base import BaseHandler


class Mediator:
    handlers: Dict[Type[BaseEvent], BaseHandler] = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def register_handler(self, event_type: Type[BaseEvent], handler: BaseHandler) -> None:
        self.handlers[event_type] = handler

    async def handle_event(self, event: BaseEvent) -> None:
        if type(event) in self.handlers:
            handler = self.handlers[type(event)]
            return await handler(event)

        raise Exception(f'Handler for event {type(event)} not registered')
