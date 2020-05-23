# mqtt_api
mqtt_api is a decorator module which converts mqtt subscriptions and messages to a flask like api.

Example: 

```python
from mqtt_api import MqttApi
import paho.mqtt.client as mqtt

# you can specify all 
# paho mqtt client options
# such as websocket connections or
# tls connections
mqttc = mqtt.Client(clean_session=True)
app = MqttApi(mqttc)


@app.route("$SYS/broker/<type>")
def broker_url_params(msg):
    print("---broker_url_params", msg.topic, msg.payload)

@app.route("$SYS/broker/+")
def broker_multi(msg,):
    print("---broker_multi", msg.topic, msg.payload)

@app.route("$SYS/broker/version")
def version(msg):
    print("---version", msg.topic, msg.payload)

@app.route("$SYS/broker/uptime")
def uptime(msg):
    print("---uptime", msg.topic, msg.payload)


if __name__ == "__main__":
    app.run( "mqtt.eclipse.org", 1883 )
```