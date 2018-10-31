from Parsers.Json.JsonParser import JsonParser


def Parse(queryName):
    queryFileDic=JsonParser("../queries.json").FileToDictionary()
    for queryItem in queryFileDic["queries"]:
        if (queryItem["name"]==queryName):
            return queryItem["query"]
    raise ModuleNotFoundError("The query - \""+queryName+"\" wasn't found")

