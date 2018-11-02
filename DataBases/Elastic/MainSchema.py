from marshmallow import Schema, fields, pprint, post_load

class QuerySchema(Schema):
    def __init__(self,data):
        super(QuerySchema, self).__init__()
        self.queryName=data["name"]
        self.data=data

    queryName = fields.Str()
    index = fields.Str()
    type = fields.Str()
    query=fields.Dict()
    @post_load
    def make_obj(self,data=None):
        i = __import__('Entities.'+self.data['type'])
        module = getattr(i, self.data['type'])
        cs = getattr(module, self.data['type'])
        return cs(**self.data)