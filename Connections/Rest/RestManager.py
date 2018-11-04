import requests

from Connections.Rest.requests.IRequests import IRequests


class RestManager(IRequests):
    def __init__(self):
        pass

    def Post(self,requestName):
        if data==None:
            res = requests.post(url,json=json)
        else:
            res = requests.post(url, data=data)