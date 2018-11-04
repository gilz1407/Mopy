from Connections.Rest.RestManager import RestManager


def RestExample():
    rest = RestManager()
    rest.Post("exampleRequest")