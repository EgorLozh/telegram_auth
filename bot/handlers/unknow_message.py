from handlers.base import BaseHandler
from events.unknow_message import UnknownMessageEvent


class UnknownMessageHandler(BaseHandler):
    async def __call__(self, event: UnknownMessageEvent):
        message = event.message
        await message.answer('Unknown message')
