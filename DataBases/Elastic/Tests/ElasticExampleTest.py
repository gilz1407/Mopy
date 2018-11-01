from DataBases.Elastic.queries.PersonByName import Person_PersonByName


def TestAskForPerson():
    p=Person_PersonByName()
    p.SetPersonName("Gil")
    p.Query()


TestAskForPerson()