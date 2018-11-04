from abc import abstractmethod
from gevent import os
from DataBases.Elastic.MainSchema import QuerySchema
from Parsers.Json.JsonParser import JsonParser


class IRequests:
    def __init__(self):
        self.isExists=False
        dir_path = os.path.dirname(os.path.realpath(__file__))
        queryFileDic = JsonParser(dir_path + "/requests.json").FileToDictionary()
        for queryItem in queryFileDic["requests"]:
            if queryItem["name"] == self.requestName:
                self.schema=QuerySchema(queryItem)
                self.queryItem=queryItem["json"]
                self.isExists=True
        if self.isExists==False:
            raise ModuleNotFoundError("The request - \"" + self.queryName + "\" wasn't found")

    @abstractmethod
    def Request(self):
        self.schema.load(self.queryItem)


