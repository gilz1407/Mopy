import time
import threading

class Listener(threading.Thread):
    def __init__(self, r, channels,callBack):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
        self.callBack=callBack

    def run(self):
        for item in self.pubsub.listen():
            self.callBack((item['channel'], item['data']))

    def unsubscribe(self,channelName):
        self.pubsub.unsubscribe(channelName)