from locust import Locust, events
from PerformanceTests.Managers.DataDriven import DataDriven


class GenerateClient(Locust):
    def __init__(self,clientName,dataDrivenfileName):
        super(GenerateClient, self).__init__()
        print("./DataDrivenFiles/"+dataDrivenfileName)
        DataDriven("./DataDrivenFiles/"+dataDrivenfileName)
        i = __import__('PerformanceTests.Clients.' + clientName)
        client = getattr(i, "Clients")
        module = getattr(client, clientName)
        cs=getattr(module,clientName)
        self.client=cs(self.host)

    def SubscribeEvents(self,failFunc,successFunc):
        events.request_failure += failFunc
        events.request_success += successFunc





