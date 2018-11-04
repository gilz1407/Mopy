from abc import abstractmethod
from gevent import os
from Connections.Rest.MainSchema import RequestSchema
from Parsers.Json.JsonParser import JsonParser

class IRequests:
    def __init__(self):
        self.isExists=False
        dir_path = os.path.dirname(os.path.realpath(__file__))
        queryFileDic = JsonParser(dir_path + "/requests.json").FileToDictionary()
        for requestItem in queryFileDic["requests"]:
            if requestItem["name"] == self.requestName:
                self.schema=RequestSchema(requestItem)
                self.requestItem=requestItem
                self.isExists=True
        if self.isExists==False:
            raise ModuleNotFoundError("The request - \"" + self.requestName + "\" wasn't found")

    @abstractmethod
    def Request(self):
        return self.schema.load(self.requestItem)


