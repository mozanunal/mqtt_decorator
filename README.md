# mqtt_decorator
[![autopep8](https://github.com/mozanunal/mqtt_decorator/actions/workflows/autopep8.yml/badge.svg)](https://github.com/mozanunal/mqtt_decorator/actions/workflows/autopep8.yml)
[![pylint](https://github.com/mozanunal/mqtt_decorator/actions/workflows/pylint.yml/badge.svg)](https://github.com/mozanunal/mqtt_decorator/actions/workflows/pylint.yml)
[![pytest](https://github.com/mozanunal/mqtt_decorator/actions/workflows/pytest.yml/badge.svg)](https://github.com/mozanunal/mqtt_decorator/actions/workflows/pytest.yml)

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

Create virtual environment (It should be done only for first installation)

```
conda create -n py38 python=3.8
```

Activate virtual environment
```
conda activate py38
```

Install this package
```
pip install -e .
```


### Deployment

In this repo issue based development is active. For any problems or new enhancements please open a issue.

Autopep8 is used for formatting.

```
autopep8 -r -i mqtt_decorator test
```

Pylint is used for linting.
```
pylint mqtt_decorator
```

### Docs

for the first time
```
sphinx-apidoc -F mqtt_decorator -o docs/source
```

just update the auto docs
```
sphinx-apidoc -f mqtt_decorator -o docs/source
```

### Licence
MIT

### Acknowledges
This package is developed using
- Python <3
- Paho-Mqtt
Heavily inspired from
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Contributors
- [mozanunal](https://github.com/mozanunal)

