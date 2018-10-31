# make sure ES is up and running
from elasticsearch import Elasticsearch

class ElasticOp():
    def __init__(self,index):
        self.index=index

    ##get back search hits that match the query.
    def GeneralQuery(self,query):
        res = Elasticsearch.search(index=self.index, body=query)
        return res

##      examples for functions usage        ##
##config to your elastic server
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#
# myMatch = byMatch('sw', 'people','name','Leia Organa')
# print('myMatch ' + str(myMatch))
#
# anyMyMatch = byMatch(index='',document= '',field='name',match='Leia Organa')
# print('anyMyMatch ' + str(anyMyMatch))
#
# count = getCountById('sw', 'people',1)
# print('count ' + str(count))
#
# anyCount = getCountById(index='', document='',id=14)
# print('anyCount ' + str(anyCount))
#
# exist = existById('sw', 'people',1)
# print('exist ' + str(exist))
#
# darthy = search('','',{"query": {"term": {"gender": {"value": "male"}}}})
# print('darthy ' + str(darthy))







