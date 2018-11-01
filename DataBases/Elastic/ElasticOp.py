from elasticsearch import Elasticsearch
from Configurations.cm import Cm

class ElasticOp():
    def __init__(self, index):
        self.conf = Cm().config['ElasticSearch']
        self.es = Elasticsearch([{'host': self.conf['host'], 'port': self.conf['port']}])
        self.index = index

    def GeneralQuery(self, query):
        res = self.es.search(index=self.index, body=query)
        return res







