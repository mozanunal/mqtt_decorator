
import paho.mqtt.client as mqtt
from functools import wraps


def on_connect(client, mqtt_api, flags, rc):
    print("Connected with result code "+str(rc))
    for topic, callback in mqtt_api.routes.items():
        client.subscribe(topic)

def on_message(client, mqtt_api, msg):
    for topic in mqtt_api.routes.keys():
        if mqtt.topic_matches_sub(topic, msg.topic):
            mqtt_api.routes[topic](msg)


class MqttApi(object):
    def __init__(self, mqtt_client):

        # init routes
        self.routes = {}

        # init mqtt
        self.mqtt_client = mqtt_client
        self.mqtt_client.user_data_set(self)
        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message


    def route(self, route_path):
        def decorator(callback_function):
            self.routes[route_path] = callback_function
        return decorator
    

    def run(self, host, port):
        self.mqtt_client.connect(
            host, port, 60
        )
        self.mqtt_client.loop_forever()