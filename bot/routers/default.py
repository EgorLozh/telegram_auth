from aiogram import Router, types

from mediator import Mediator
from events.unknow_message import UnknownMessageEvent

default_router = Router()


@default_router.message()
async def default(message: types.Message):
    event = UnknownMessageEvent(message=message)
    mediator = Mediator()
    await mediator.handle_event(event)
