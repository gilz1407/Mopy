from marshmallow import Schema, fields, post_load
from Connections.Rest.RestManager import RestManager

class RequestSchema(Schema):
    def __init__(self,data):
        super(RequestSchema, self).__init__()
        self.name=data["name"]
        self.type = data["type"]
        self.url = data["url"]
        self.js = data["js"]
        self.data = data["data"]
        self.params=data["params"]
        self.apiParams=data["apiParams"]
        self.dataItem = data
        self.rest=RestManager()

    name = fields.Str()
    type = fields.Str()
    url = fields.Str()
    js = fields.Dict()
    data = fields.Str()
    params = fields.Dict()
    apiParams=fields.Str()

    @post_load
    def make_obj(self,data=None):
        print("im in "+self.type)
        if self.type == "post":
            return self.rest.Post(self.dataItem)
        elif self.type == "get":
            return self.rest.Get(self.dataItem)
        elif self.type == "delete":
            return self.rest.Delete(self.dataItem)
