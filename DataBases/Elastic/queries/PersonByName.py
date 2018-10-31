from DataBases.Elastic.Entities.Person import Person
from DataBases.Elastic.IQuery import IQuery

class Person_PersonByName(IQuery):

    def __init__(self):
        super().__init__(self.__class__)

    def SetPersonName(self,name):
        self.query["query"]["match"]["name"]=name

    def Query(self):
        res=self.op.GeneralQuery(self.query)
        return Person.Deserialize(res)