import redis
from MessageBrokers.Redis.RedisManager import Listener

def redisTest():
    r = redis.Redis()
    client = Listener(r, ['test', 'test2'])
    client.start()

    r.publish('gil', 'yeaa')
    r.publish('test', 'this will reach the listener')
    r.publish('test2', 'this will work')
    r.publish('fail', 'this will not')
    r.publish('test', 'KILL')

redisTest()