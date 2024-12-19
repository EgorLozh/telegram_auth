from aiogram.types import Message

from handlers.base import BaseHandler
from events.user_auth import UserAuthEvent


class UserAuthHandler(BaseHandler):
    async def __call__(self, event: UserAuthEvent) -> None:
        message: Message = event.message
        token = event.token
        await message.answer('Authorized'+ token)