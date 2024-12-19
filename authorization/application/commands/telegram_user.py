from authorization.application.commands.base import BaseCommand


class CreateTelegramUserCommand(BaseCommand):
    telegram_id: int
    username: str
    first_name: str
    token: str
