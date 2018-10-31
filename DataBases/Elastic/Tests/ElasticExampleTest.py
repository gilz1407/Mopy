from DataBases.Elastic.queries.PersonByName import Person_PersonByName


def TestAskForPerson():
    #EsHelper("customer").GeneralQuery("queryDemo",{"name":"John Doe","JobTitle":"SW"})
    p=Person_PersonByName()
    p.SetPersonName("Gil")
    p.Query()


TestAskForPerson()