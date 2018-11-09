import json

class JsonParser:
    def __init__(self,fileName=None):
        self.fileName=fileName

    def FileToDictionary(self):
        f = open(self.fileName)
        return json.load(f)  # to python object (dictionary)

    def FileToString(self):
        f = open(self.fileName)
        tempdic=json.load(f)  # to python dictionary
        return json.dumps(tempdic)

    def StringToDictionary(self,jsonStr):
        return json.loads(jsonStr)

    def DictionaryToFile(self,dic,filePath):
        toFile = open(filePath,'w')
        json.dump(dic,toFile)

    def StringToFile(self,str,filePath):
        dic=self.StringToDictionary(str)
        self.DictionaryToFile(dic,filePath)