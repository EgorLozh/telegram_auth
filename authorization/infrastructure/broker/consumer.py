import json
import pika

from authorization.infrastructure.broker.base import BaseBrokerClient
from authorization.infrastructure.broker.mediator import Mediator



class Consumer(BaseBrokerClient):
    mediator: Mediator = Mediator()

    def call_back(self, ch, method, properties, body):

        json_str = body.decode('utf-8')
        event_dict: dict = json.loads(json_str)

        event_class = self.mediator.get_event_type(event_dict['event_name'])

        event = event_class(**event_dict)

        self.mediator.handle_event(event)

    def consume(self):
        try:
            if not self.channel or self.channel.is_closed:
                self.connect()

            self.channel.basic_consume(queue=self.queue, on_message_callback=self.call_back, auto_ack=True)
            self.channel.start_consuming()

        except pika.exceptions.ConnectionClosedByBroker:
            self.reconnect()
            self.consume()
        except pika.exceptions.AMQPChannelError as err:
            self.reconnect()
        except pika.exceptions.AMQPConnectionError as err:
            self.reconnect()
