# mqtt_decorator
mqtt_decorator is a decorator module which converts mqtt subscriptions and messages to a [Flask](https://flask.palletsprojects.com/en/1.1.x/) like api.

### Demo

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

### Installing


### Development


### Deployment

```
pip install -e .
```

### Licence


### Acknowledges
This package is developed using
- Python <3
- Paho-Mqtt
Heavily inspired from
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
