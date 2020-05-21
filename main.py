

from mqtt_api import MqttApi
import paho.mqtt.client as mqtt

mqttc = mqtt.Client(clean_session=True)
app = MqttApi(mqttc)


@app.route("$SYS/broker/+")
def broker_multi(msg):
    print("---broker_multi", msg.topic, msg.payload)

@app.route("$SYS/broker/version")
def version(msg):
    print("---version", msg.topic, msg.payload)

@app.route("$SYS/broker/uptime")
def uptime(msg):
    print("---uptime", msg.topic, msg.payload)


if __name__ == "__main__":
    app.run( "mqtt.eclipse.org", 1883 )

    

