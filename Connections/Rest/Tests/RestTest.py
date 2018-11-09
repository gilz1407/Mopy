from Connections.Rest.requests.ExampleRequest import ExampleRequest


er =ExampleRequest()
er.SetCategoryName("newCategory")
er.SetId(12)
er.SetPetName("Nisui")
er.SetTagName("MyPets")


res = er.Request()
print (res)


