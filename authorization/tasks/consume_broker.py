from celery import shared_task
from authorization.infrastructure.broker.consumer import Consumer
from configs.settings import Settings


@shared_task
def run_consumer():
    try:
        print("Starting Consumer...")
        settings = Settings()
        print(f"Settings: {settings}")
        consumer = Consumer(
            user=settings.RABBIT_USER,
            password=settings.RABBIT_PASSWORD,
            host=settings.RABBIT_HOST,
            port=settings.RABBIT_PORT,
            queue=settings.RABBIT_QUEUE
        )
        print(f"Consumer initialized with queue: {settings.RABBIT_QUEUE}")
        consumer.consume()
    except Exception as e:
        print(f"Error in run_consumer task: {str(e)}")
        raise e
