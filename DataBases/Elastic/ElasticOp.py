from elasticsearch import Elasticsearch
from Configurations.cm import Cm

class ElasticOp():
    def __init__(self, index):
        self.section = 'ElasticSearch'
        self.conf = Cm().config
        self.es = Elasticsearch([{'host': self.conf[self.section]['host'], 'port': self.conf[self.section]['port']}])
        self.index = index

    def GeneralQuery(self, query):
        res = self.es.search(index=self.index, body=query)
        return res







