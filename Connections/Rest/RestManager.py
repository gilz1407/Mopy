import requests

class RestManager():
    def __init__(self):
        pass

    def Post(self,data):
        return requests.post(data["url"],json=data["js"])

    def Get(self,data):
        pass