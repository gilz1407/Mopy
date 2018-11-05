from Connections.Rest.requests.IRequests import IRequests

class GetPet(IRequests):
    def __init__(self):
        self.requestName=self.__class__.__name__
        super(GetPet,self).__init__()

    def SetPetId(self,id):
        self.requestItem["apiParams"] = "/"+str(id)