from __future__ import absolute_import, unicode_literals
from celery.signals import worker_ready
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_auth.telegram_auth.celery_settings')

app = Celery('telegram_auth')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['authorization.tasks'])


@worker_ready.connect
def run_task_on_startup(sender, **kwargs):
    app.send_task('authorization.tasks.consume_broker.run_consumer', args=([]))
