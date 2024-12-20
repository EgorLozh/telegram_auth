from aiogram.types import Message

from handlers.base import BaseHandler
from events.user_auth import UserAuthEvent
from services import post_request


class UserAuthHandler(BaseHandler):
    async def __call__(self, event: UserAuthEvent) -> None:
        message: Message = event.message
        token = event.token
        data = {
            'telegram_id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'token': token
        }
        response = await post_request(data=data)
        await message.answer(str(response))