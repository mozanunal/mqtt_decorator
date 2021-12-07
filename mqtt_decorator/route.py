
import re
import json
import inspect


class Route(object):
    def __init__(self, url, func, qos=2):
        """Route class to handle and verify routes
        available options:
        - "$SYS/broker/version"
        - "$SYS/<broker>/<type>"
        - "$SYS/broker/+"
        - "$SYS/#"
        It also stores the function which will be
        exevuted when a new message is arrived from
        mqtt.

        Arguments:
            url {str} -- url in format mqtt_api routes
            func {function} -- function to executed when the
            package is arrived

        Keyword Arguments:
            qos {int} -- QOS (default: {2})
        """
        self.url = url
        self.topic = Route.url_to_topic(url)
        self.args = Route.url_to_args(url)
        self.func = func
        self.qos = qos
        self._topic_parsed = self.topic.split("/")
        self._url_parsed = self.url.split("/")
        self._check_func()

    def exec(self, msg):
        """Gets only mqtt msg as argument 

        Arguments:
            msg {paho.mqtt.client.MQTTMessage} -- received mqtt message
        """
        msg_topic_parsed = msg.topic.split("/")
        func_args = {
            key: self._find_arg_value(key, msg_topic_parsed)
            for key in self.args}
        func_args["msg"] = msg
        self.func(**func_args)

    def _check_func(self):
        """Check the structure of the 
        callback function.
        - Check the arguments are correct


        Raises:
            AttributeError: it raises if the
            arguments of the function are not
            correct
        """
        # check arguments
        func_info = inspect.getargspec(self.func)
        for arg in self.args:
            if arg not in func_info.args:
                error_msg = "Arguments are not correct! "
                error_msg += "url: {} ".format(self.url)
                raise AttributeError(error_msg)

    def _find_arg_value(self, arg, msg_topic_parsed):
        """Get value from topic string

        Arguments:
            arg {str} -- function argument key
            msg_topic_parsed {list} -- received message topic parsed
            with "\" 
        """
        idx = self._url_parsed.index("<{}>".format(arg))
        return msg_topic_parsed[idx]

    def __repr__(self):
        return json.dumps(self.__dict__, default=str)

    # def func_wrapper(self, func):
    #     def route_callback(msg):
    #         #func.globals.update({'msg':msg})
    #         return func()
    #     return route_callback

    @staticmethod
    def url_to_args(url):
        args = re.findall("<(.*?)>", url)
        return args

    @staticmethod
    def url_to_topic(url):
        topic = re.sub("<(.*?)>", "+", url)
        return topic
