from elasticsearch import Elasticsearch
from Configurations.cm import Cm

class ElasticOp():
    def __init__(self, index):
        self.conf = Cm().config['ElasticSearch']
        self.es = Elasticsearch([{'host': self.conf['host'], 'port': self.conf['port']}])
        self.index = index

    def GeneralQuery(self, query):
        return self.es.search(index=self.index, body=query)

    def CreateIndex(self,indexName,number_of_shards=1,number_of_replicas=0):
        request_body = {
            "settings": {
                "number_of_shards": number_of_shards,
                "number_of_replicas": number_of_replicas
            }
        }
        return self.es.create(index=indexName,body=request_body)







