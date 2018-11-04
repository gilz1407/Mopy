from Connections.Rest.requests.IRequests import IRequests

class ExampleRequest(IRequests):
    def __init__(self):
        self.requestName=self.__class__.__name__
        super(ExampleRequest,self).__init__()


    def setKeyValue(self,tuple):
        match=self.queryItem["query"]["match"]
        match.update({tuple[0]:tuple[1]})