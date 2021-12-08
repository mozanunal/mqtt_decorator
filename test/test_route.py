
from paho.mqtt.client import MQTTMessage
from mqtt_decorator.route import Route


def test_url_to_args():
    assert Route.url_to_args("test/<hey>/<yoo>") == ["hey", "yoo"]
    assert Route.url_to_args("") == []
    assert Route.url_to_args("<hey>") == ["hey"]
    assert Route.url_to_args("<hey>/") == ["hey"]
    assert Route.url_to_args("$SYS/<hey>/") == ["hey"]
    assert Route.url_to_args("$SYS]]/<hey>/") == ["hey"]
    
def test_url_to_topic():
    assert Route.url_to_topic("test/<hey>/<yoo>") == "test/+/+"
    assert Route.url_to_topic("") == ""
    assert Route.url_to_topic("<hey>") == "+"
    assert Route.url_to_topic("<hey>/") == "+/"
    assert Route.url_to_topic("$SYS/<hey>/") == "$SYS/+/"
    assert Route.url_to_topic("$SYS]]/<hey>/") == "$SYS]]/+/"


def func_to_arg_tester(url, received_topic, expected_result):
    route = Route(url, lambda hey, yoo: (hey, yoo) )
    msg = MQTTMessage(topic=received_topic)
    result = route.find_func_args(msg)
    result
    assert  == expected_result

def test_find_func_arguments():
    func_to_arg_tester( "test/<hey>/<yoo>", b"test/1/2", {"hey":"1", "yoo": "2"}  )