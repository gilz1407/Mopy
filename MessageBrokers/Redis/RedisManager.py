import time
import threading

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)


    def work(self, item):
        print (item['channel'], ":", item['data'])

    def run(self):
        for item in self.pubsub.listen():
            print ("Item:   ",item)
            self.work(item)
            time.sleep(3)

    def unsubscribe(self,channelName):
        self.pubsub.unsubscribe(channelName)