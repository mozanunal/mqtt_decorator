
import re
import json
import inspect


class Route(object):
    def __init__(self, url, func, qos=2):
        self.url = url
        self.topic = Route.url_to_topic(url)
        self.args = Route.url_to_args(url)
        self.func = func #self.func_wrapper(func)
        self.qos = qos
        self.check_func()
    
    def check_func(self):
        # check arguments
        func_info = inspect.getargspec(self.func)
        for arg in self.args:
            if arg not in func_info.args:
                error_msg = "Arguments are not correct! "
                error_msg += "url: {} ".format(self.url)
                raise AttributeError(error_msg)


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

