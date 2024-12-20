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
            user=settings.BOT_BROKER_USER,
            password=settings.BOT_BROKER_PASSWORD,
            host=settings.RABBIT_HOST,
            port=settings.AMQP_PORT,
            queue=settings.RABBIT_QUEUE
        )
        print(f"Consumer initialized with queue: {settings.RABBIT_QUEUE}")
        consumer.consume()
    except Exception as e:
        print(f"Error in run_consumer task: {str(e)}")
        raise e
