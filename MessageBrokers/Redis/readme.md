**Redis**

A wrapper for pub\sub management with redis.

**Getting Started**
 
**Prerequisites**

If you don't have Redis server yet:
1. Install "Redis" server by using the tutorial: https://dingyuliang.me/redis-3-2-install-redis-windows/

**Installing**

For using/developing on the redis wrapper: 
Install "redis" package.

Or for more general preparation please install:
    "pip install requirements.txt" 

**Structure**

One file called "RedisManager" witch is a wrapper for redis and one example of using :
```python
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
``` 
Every test can define the function that will take processing messages from redis.
In order to kill the redis thread unsubscribe from all channels is needed.

**Author**
Gil zur




    
    


 









 
