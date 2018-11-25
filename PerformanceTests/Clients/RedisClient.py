from gevent import time

from PerformanceTests.Managers.StopWatch import stopwatch


class RedisClient:
    def __init__(self, host):
        host = host.split(':')
        self.host = str(host[0])
        self.port = int(host[1])

    @stopwatch
    def CheckQueue(self,str):
        print(str)
        time.sleep(1)
        return True

    def new_connection(self):
        print("new connection to " + self.host + ":" + str(self.port))
        time.sleep(1)
        return None

    @stopwatch
    def publish(self, set):
        print("uploading: " + set)
        time.sleep(2)
        return True

    def close_connection(self):
        print("connection closed")
        time.sleep(1)
        return None