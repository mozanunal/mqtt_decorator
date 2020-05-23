
import re

class Route(object):
    def __init__(self, url, func, qos=2):
        self.url = url
        self.topic = url #Route.url_to_topic(url)
        self.func = self.func_wrapper(func)
        self.qos = qos
    
    def func_wrapper(self, func):
        def route_callback(msg):
            #func.globals.update({'msg':msg})
            return func()
        return route_callback

    # @staticmethod
    # def url_to_topic(url):
    #     topic = re("<*>", "+", url)
    #     print(url, topic)
    #     return topic

