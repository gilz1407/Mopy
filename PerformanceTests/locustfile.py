#locust --host=localhost:8000
import os
import sys

from locust import TaskSet, task, TaskSequence, seq_task
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PerformanceTests.Managers.DataDriven import DataDriven
from PerformanceTests.Managers.GenerateClient import GenerateClient

class ProtocolTasks1(TaskSequence):
    @seq_task(1)
    def MyThirdTask(self):
        str = DataDriven().Get()
        print("seq 1")
        self.client.CheckQueue(str["first name"])


    @seq_task(2)
    def MyFourTask(self):
        print("seq 2")
        self.client.CheckQueue("CheckQueue")

class ProtocolTasks2(TaskSet):
    @task
    def MyFirstTask(self):
        self.client.new_connection()
        str = DataDriven().Get()
        self.client.publish("Publish to redis-"+str['first name'])
        self.client.close_connection()

    @task
    def MySecondTask(self):
        print("It's a kind of magic")

class ProtocolUser(GenerateClient):
    def __init__(self):
        super(ProtocolUser,self).__init__("RedisClient","names.csv")
    task_set = ProtocolTasks1
    host = 'localhost:8000'
    min_wait = 0
    max_wait = 0

class ProtocolUser1(GenerateClient):
    def __init__(self):
        super(ProtocolUser1,self).__init__("RedisClient","names.csv")

    host = 'localhost:8000'
    task_set = ProtocolTasks2
    min_wait = 0
    max_wait = 0

