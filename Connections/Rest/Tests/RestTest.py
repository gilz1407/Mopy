from Connections.Rest.requests.CreateNewPet import CreateNewPet
from Connections.Rest.requests.GetPet import GetPet

def RestExample():
    er = CreateNewPet()

    er.SetCategoryName("newCategory")
    er.SetId(12)
    er.SetPetName("Nisui")
    er.SetTagName("MyPets")

    res = er.Request()
    print(res)

    er = GetPet()
    er.SetPetId(12)
    res = er.Request()
    print(res.content)

RestExample()