import redis
from MessageBrokers.Redis.RedisManager import Listener

#The function get the current item on queue (Tuple-> (ChannelName,Data))

def MyCare(tup):
    print("Channel: "+str(tup[0])+" Data: "+str(tup[1]))

def redisTest():
    r = redis.Redis()   # Connecting to localhost redis server.
    client = Listener(r, ['test', 'test2'],MyCare)  # Create a listener for number of channels on sperate thread.
    client.start()  # Start listening.

    # Publish different data on number of channels.
    r.publish('gil', 'yeaa')
    r.publish('test', 'this will reach the listener')
    r.publish('test2', 'this will work')
    r.publish('fail', 'this will not')
    r.publish('test', 'KILL')

    # After handling all of the messages from redis - unsubscribe will stop the redis thread
    client.unsubscribe('test')
    client.unsubscribe('test2')

redisTest()