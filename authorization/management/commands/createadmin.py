import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create admin'

    def handle(self, *args, **options):
            load_dotenv()
            user = get_user_model()
            if user.objects.filter(username=os.getenv('ADMIN_NAME')).exists():
                print(f'Admin {os.getenv("ADMIN_NAME")} already exists')
                return
            user.objects.create_superuser(username=os.getenv('ADMIN_NAME'), password=os.getenv('ADMIN_PASSWORD'))
            print(f'Admin {os.getenv("ADMIN_NAME")} created')