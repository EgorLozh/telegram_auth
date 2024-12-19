from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from services import get_sessionid
from events.user_auth import UserAuthEvent
from mediator import Mediator


auth_router = Router()
sessionid = get_sessionid()


@auth_router.message(Command(commands=["start"]))
async def auth(message: types.Message, command: CommandObject) -> None:
    token = command.args
    event = UserAuthEvent(message=message, token=token, session_id=sessionid)
    mediator = Mediator()
    return await mediator.handle_event(event)
    