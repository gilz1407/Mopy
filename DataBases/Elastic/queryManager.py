from gevent import os

from Parsers.Json.JsonParser import JsonParser


def Parse(queryName):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    queryFileDic = JsonParser(dir_path+"/queries.json").FileToDictionary()
    for queryItem in queryFileDic["queries"]:
        if queryItem["name"] == queryName:
            return queryItem["query"]
    raise ModuleNotFoundError("The query - \""+queryName+"\" wasn't found")

