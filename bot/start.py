import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from events.user_auth import UserAuthEvent
from handlers.user_auth import UserAuthHandler
from mediator import Mediator
from routers.default import default_router
from routers.auth import auth_router
from events.unknow_message import UnknownMessageEvent
from handlers.unknow_message import UnknownMessageHandler


def init_mediator() -> Mediator:
    mediator = Mediator()

    mediator.register_handler(UnknownMessageEvent, UnknownMessageHandler())
    mediator.register_handler(UserAuthEvent, UserAuthHandler())

    return mediator

async def start_bot() -> None:

    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    init_mediator()

    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(auth_router)
    dp.include_router(default_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(start_bot())
