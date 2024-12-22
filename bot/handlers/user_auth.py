import os
from dotenv import load_dotenv
from broker.publisher import Publisher
from aiogram.types import Message

from handlers.base import BaseHandler
from events.user_auth import UserAuthEvent


class UserAuthHandler(BaseHandler):
    async def __call__(self, event: UserAuthEvent) -> None:
        load_dotenv()
        publisher = Publisher(
            host=os.getenv('RABBIT_HOST'),
            port=os.getenv('AMQP_PORT'),
            user=os.getenv('RABBIT_USER'),
            password=os.getenv('RABBIT_PASSWORD'),
            queue=os.getenv('RABBIT_QUEUE')
        )
        message: Message = event.message
        token = event.token
        data = {
            'event_name': 'create_user',
            'telegram_id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'token': token
        }

        publisher.publish(data)

        await message.answer('Вы успешно авторизовались!')