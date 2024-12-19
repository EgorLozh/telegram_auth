from dataclasses import dataclass, field
from typing import Dict, List, Type
from authorization.application.command_handlers.base import BaseCommandHandler
from authorization.application.query_handler.base import BaseQueryHandler
from authorization.application.commands.base import BaseCommand
from authorization.application.queries.base import BaseQuery


@dataclass
class Mediator:
    command_handlers: Dict[Type[BaseCommand], BaseCommandHandler] = field(default_factory=dict)
    query_handlers: Dict[Type[BaseQuery], BaseQueryHandler] = field(default_factory=dict)

    def register_command(self, commnad_type: Type[BaseCommand], handler: BaseCommandHandler) -> None:
        self.command_handlers[commnad_type] = handler

    def register_query(self, query_type: Type[BaseQuery], handler: BaseQueryHandler) -> None:
        self.query_handlers[query_type] = handler

    def handle_command(self, command: BaseCommand) -> None:
        if type(command) in self.command_handlers:
            handler = self.command_handlers[type(command)]
            return handler(command)
        
        raise Exception(f'Handler for command {type(command)} not registered')
        
    def handle_query(self, query: BaseQuery) -> None:
        if type(query) in self.query_handlers:
            handler = self.query_handlers[type(query)]
            return handler(query)

        raise Exception(f'Handler for query {type(query)} not registered')
