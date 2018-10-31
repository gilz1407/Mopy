from Parsers.Json.JsonParser import JsonParser


def ReadFromFile():
    p=JsonParser("../JsonTest.json")
    #Reading the file content as dictionary.
    pyDic=p.FileToDictionary()
    pyDic["workers"][0]["name"]="New Title"
    pyStr = p.FileToString()
    p.DictionaryToFile(pyDic,"../resultDic.json")
    p.StringToFile(pyStr,"../resultStr.json")

ReadFromFile()

