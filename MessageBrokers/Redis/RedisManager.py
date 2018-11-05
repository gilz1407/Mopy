import time
import threading


class Listener(threading.Thread):
    lstMessages = []

    def __init__(self, r, channels, callBack=None):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
        self.callBack = callBack

    def run(self):
        global lstMessages
        for item in self.pubsub.listen():
            Listener.lstMessages.append(item)
            if self.callBack is not None:
                self.callBack((item['channel'], item['data']))

    def GetLastMessages(self):
        temp = Listener.lstMessages
        Listener.lstMessages = []
        return temp

    def unsubscribe(self, channelName):
        self.pubsub.unsubscribe(channelName)
