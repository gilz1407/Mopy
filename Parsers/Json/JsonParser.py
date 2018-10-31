import json
class JsonParser:
    def __init__(self,fileName):
        self.f = open(fileName)

    def FileToDictionary(self):
        return json.load(self.f)  # to python object (dictionary)

    def FileToString(self):
        tempDic= json.load(self.f)  # to python dictionary
        return json.dumps(tempDic)

    def StringToDictionary(self,jsonStr):
        return json.loads(jsonStr)

    def DictionaryToFile(self,dic,filePath):
        self.toFile = open(filePath)
        json.dump(str(dic),self.toFile)

    def StringToFile(self,str,filePath):
        dic=json.loads(str)
        json.dump(str(dic),filePath)