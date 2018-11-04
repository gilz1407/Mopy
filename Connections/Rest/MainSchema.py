from marshmallow import Schema, fields, post_load

from DataBases.Elastic.ElasticOp import ElasticOp


class RequestSchema(Schema):
    def __init__(self,data):
        super(RequestSchema, self).__init__()
        self.requestName=data["name"]
        self.type = data["type"]
        self.url = data["url"]
        self.json = data["json"]
        self.data = data["data"]

    requestName = fields.Str()
    type = fields.Str()
    url = fields.Str()
    json = fields.Dict()
    data = fields.Dict()

    @post_load
    def make_obj(self,data=None):
        op=ElasticOp(self.index)
        op.GeneralQuery(self.query)
        i = __import__('DataBases.Elastic.Entities.'+self.data['type'])
        i = getattr(i,'Elastic')
        module = getattr(i, 'Entities')
        cs = getattr(module, self.data['type'])
        cs = getattr(cs, self.data['type'])
        return cs(**self.data)