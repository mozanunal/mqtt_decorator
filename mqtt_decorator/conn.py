
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


class MqttDecorator(object):
    def __init__(self, mqtt_client):
        """Mqtt Decorator is the class which convert mqtt
        subscriptions to a Flask like api. 

        Arguments:
            mqtt_client {paho.mqtt.client.Client} -- [description]

        mqtt_decorator is a decorator module which converts 
        mqtt subscriptions and messages to a Flask like api.

        ```python
        from mqttdecorator import MqttDecorator
        import paho.mqtt.client as mqtt

        # you can specify all 
        # paho mqtt client options
        # such as websocket connections or
        # tls connections
        mqttc = mqtt.Client(clean_session=True)
        app = MqttDecorator(mqttc)

        @app.route("$SYS/<broker>/<type>")
        def broker_url_params(msg, broker, type):
            print("---broker_url_params", msg.topic, msg.payload)
            print("--broker", broker)
            print("--type", type)

        @app.route("$SYS/broker/version")
        def version(msg):
            print("---version", msg.topic, msg.payload)

        @app.route("$SYS/broker/uptime")
        def uptime(msg):
            print("---uptime", msg.topic, msg.payload)


        if __name__ == "__main__":
            app.run( "mqtt.eclipse.org", 1883 )

        ```
        """
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