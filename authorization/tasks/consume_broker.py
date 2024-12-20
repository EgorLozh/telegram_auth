from celery import shared_task
from authorization.infrastructure.broker.consumer import Consumer
from configs.settings import Settings

@shared_task
def run_consumer():
    settings = Settings()
    consumer = Consumer(
        user=settings.RABBIT_USER,
        password=settings.RABBIT_PASSWORD,
        host=settings.RABBIT_HOST,
        port=settings.RABBIT_PORT,
        queue=settings.RABBIT_QUEUE
    )
    consumer.consume()