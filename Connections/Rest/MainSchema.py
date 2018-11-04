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
        self.dataItem = data
        self.rest=RestManager()

    name = fields.Str()
    type = fields.Str()
    url = fields.Str()
    js = fields.Dict()
    data = fields.Str()

    @post_load
    def make_obj(self,data=None):
        switcher = {
                "post": self.rest.Post(self.dataItem),
                "get": self.rest.Get(self.dataItem)
            }
        return switcher.get(self.type)