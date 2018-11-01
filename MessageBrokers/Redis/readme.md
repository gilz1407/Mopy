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

def redisTest():
    r = redis.Redis()
    client = Listener(r, ['test', 'test2'])
    client.start()

    r.publish('gil', 'yeaa')
    r.publish('test', 'this will reach the listener')
    r.publish('test2', 'this will work')
    r.publish('fail', 'this will not')
    r.publish('test', 'KILL')
``` 




Query example:
```json
{
  "queries":[
    {
      "name":"PersonByName",
      "query":{
        "query": {
          "match":
          {
            "name":""
          }
        }
      }
    }
  ]
}
```

After the relevant query was added , suitable class needs to be defined on queries folder.
Structure of the class name {index}_{queryName}:

```python
from DataBases.Elastic.Entities.Person import Person
from DataBases.Elastic.IQuery import IQuery

#Person->index  PersonByName->The name of the query
class Person_PersonByName(IQuery):  

    def __init__(self):
        super().__init__(self.__class__)

    def SetPersonName(self,name):
        self.query["query"]["match"]["name"]=name

    def Query(self):
        res=self.op.GeneralQuery(self.query)
        return Person.Deserialize(res)
```
  Tם your attention: "Query" method must be implemented. 
        
In order to get the query result as object:
1. Every entity needs to implement IEntity and as a result implement 
    ```python
    @classmethod
    def Deserialize(cls,data):
        tempPerson =cls(data["name"])
        return tempPerson
     ``` 
   The method above takes the Json response from the elastic query and creates object from the suitable class "Person"

**Author**
Gil zur




    
    


 









 
