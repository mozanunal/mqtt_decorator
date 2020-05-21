
import paho.mqtt.client as mqtt
from functools import wraps


def on_connect(client, mqtt_api, flags, rc):
    print("Connected with result code "+str(rc))
    for topic, route in mqtt_api.routes.items():
        client.subscribe(topic)

def on_message(client, mqtt_api, msg):
    for topic, route in mqtt_api.routes.items():
        if mqtt.topic_matches_sub(topic, msg.topic):
            route.func(msg)


class Route(object):
    def __init__(self, topic, func, qos=2):
        self.topic = topic
        self.func = func
        self.qos = qos

class MqttApi(object):
    def __init__(self, mqtt_client):

        # init routes
        self.routes = {}

        # init mqtt
        self.mqtt_client = mqtt_client
        self.mqtt_client.user_data_set(self)
        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message


    def route(self, route_path, qos=2):
        def decorator(callback_function):
            route = Route(route_path, callback_function, qos=qos)
            self.routes[route_path] = route
        return decorator
    

    def run(self, host, port):
        self.mqtt_client.connect(
            host, port, 60
        )
        self.mqtt_client.loop_forever()