from DataBases.Elastic.IEntity import IEntity


class Person(IEntity):
    def __init__(self,name):
        self.name = name

    @classmethod
    def Deserialize(cls,data):
        tempPerson =cls(data["name"])
        return tempPerson



