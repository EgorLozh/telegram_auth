from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from events.user_auth import UserAuthEvent
from mediator import Mediator


auth_router = Router()


@auth_router.message(Command(commands=["start"]))
async def auth(message: types.Message, command: CommandObject) -> None:
    token = command.args
    event = UserAuthEvent(message=message, token=token)
    mediator = Mediator()
    return await mediator.handle_event(event)
    