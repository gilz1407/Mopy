from abc import abstractmethod
import re
from DataBases.Elastic.ElasticOp import ElasticOp
from DataBases.Elastic.queryManager import Parse


class IQuery:
    def __init__(self,clsName):
        res=re.search('<class(.*)\'([a-z,A-Z,.,_]+)\'>',str(clsName))
        clsName=res.groups(2)[1].split(".")[-1]
        self.index=str(clsName).split("_")[0]
        self.queryName=str(clsName).split("_")[1]
        self.op = ElasticOp(index=self.index)
        self.query = Parse(self.queryName)

    @abstractmethod
    def Query(self):raise NotImplementedError("The method - \"Query\" wasn't implemented")

