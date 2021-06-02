

from mqtt_decorator import MqttDecorator
import paho.mqtt.client as mqtt

# you can specify all 
# paho mqtt client options
# such as websocket connections or
# tls connections
mqttc = mqtt.Client(clean_session=True)
app = MqttDecorator(mqttc)

@app.route("$SYS/<broker>/<type>")
def broker_url_params(msg, broker, type):
    print("---broker_url_params", broker, msg.topic)

@app.route("$SYS/broker/version")
def version(msg):
    print("---version", msg.topic, msg.payload)

@app.route("$SYS/broker/uptime")
def uptime(msg):
    print("---uptime", msg.topic, msg.payload)


if __name__ == "__main__":
    
    import os
    from dotenv import load_dotenv

    load_dotenv()
    
    app.run( 
        os.environ['TEST_MQTT_HOST'], 
        int(os.environ['TEST_MQTT_PORT'] )
    )

    

