from Connections.Rest.requests.IRequests import IRequests

class DeleteVideo(IRequests):
    def __init__(self):
        self.requestName=self.__class__.__name__
        super(DeleteVideo,self).__init__()

    def SetVideoId(self, videoId):
        self.requestItem["js"]["id"] = videoId