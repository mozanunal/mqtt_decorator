
import paho.mqtt.client as mqtt
from functools import wraps

from .route import Route

def on_connect(client, mqtt_api, flags, rc):
    print("Connected with result code "+str(rc))
    for topic, route in mqtt_api.routes.items():
        client.subscribe(topic)

def on_message(client, mqtt_api, msg):
    for topic, route in mqtt_api.routes.items():
        if mqtt.topic_matches_sub(topic, msg.topic):
            route.exec(msg)


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
        """Decorator to create routes

        Arguments:
            route_path {str} -- string mqtt route
            formatted like Flask route 

        Keyword Arguments:
            qos {int} -- Quality of service. Please see mqtt
            documentation further details (default: {2})
        """
        def decorator(callback_function):
            route = Route(route_path, callback_function, qos=qos)
            self.routes[route.topic] = route
        return decorator
    

    def run(self, host, port):
        """Runs the mqtt api. It blocks forever.

        Arguments:
            host {str} -- mqtt host to connect
            port {int} -- mqtt port to connect
        """
        self.mqtt_client.connect(
            host, port, 60
        )
        self.mqtt_client.loop_forever()