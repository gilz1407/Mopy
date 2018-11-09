from Connections.Rest.requests.IRequests import IRequests

class CreateNewPet(IRequests):
    def __init__(self):
        self.requestName=self.__class__.__name__
        super(CreateNewPet,self).__init__()

    def SetPetName(self, name):
        self.requestItem["js"]["name"]=name

    def SetCategoryName(self, name):
        self.requestItem["js"]["category"]["name"] = name

    def SetTagName(self, tagName):
        self.requestItem["js"]["tags"][0]["name"] = tagName

    def SetId(self, id):
        self.requestItem["js"]["id"] = id
        self.requestItem["js"]["tags"][0]["id"] = id


