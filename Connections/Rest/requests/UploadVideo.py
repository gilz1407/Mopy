from Connections.Rest.requests.IRequests import IRequests

class UploadVideo(IRequests):
    def __init__(self):
        self.requestName=self.__class__.__name__
        super(UploadVideo,self).__init__()

    def SetFileName(self, name):
        self.requestItem["js"]["fileName"]=name

    def SetDescription(self, name):
        self.requestItem["js"]["description"] = name

    def SetTitle(self, tagName):
        self.requestItem["js"]["title"] = tagName