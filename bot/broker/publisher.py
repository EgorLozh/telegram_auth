import json
import pika

from broker.base import BaseBrokerClient


class Publisher(BaseBrokerClient):

    def publish(self, message_dict: dict):
        try:
            if not self.channel or self.channel.is_closed:
                self.connect()

            message = json.dumps(message_dict)

            self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
        except pika.exceptions.ConnectionClosed as e:
            self.reconnect()
    