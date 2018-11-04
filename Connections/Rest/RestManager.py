import requests

class RestManager():
    def __init__(self,url=None):
        if url!=None:
            self.url=url

    def Post(self,data):
        return requests.post(data["url"],json=data["js"])

    def Get(self,data):
        #PARAMS = {'address': location} - example
        return requests.get(data["url"], params=data["params"])

    def Put(self,data):
        pass

    def Delete(self,data):
        pass