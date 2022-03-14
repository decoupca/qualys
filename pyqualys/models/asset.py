from pyqualys.core.endpoint import Endpoint


class Asset(object):
    def __init__(self, api):
        self.host = Endpoint(api, "/api/2.0/fo/asset/host/", 'host')
        self.group = Endpoint(api, "/api/2.0/fo/asset/group/", 'asset_group')
        self.ip = Endpoint(api, '/api/2.0/fo/asset/ip/', 'ip', 'ip_set')

#class Host(Endpoint):
#    def __init__(self, api):
#        self.endpoint = "/api/2.0/fo/asset/host/"
#
#    def list(self):
#        response = self.api.list(self.endpoint)
#        index = response["HOST_LIST_OUTPUT"]["RESPONSE"]
#        data = response["HOST_LIST_OUTPUT"]["RESPONSE"]["HOST_LIST"]["HOST"]
#        return self.api.parse_response(index=index, data=data)
#
#
#class Group(Endpoint):
#    def __init__(self, api):
#        self.endpoint = "/api/2.0/fo/asset/group/"
#
#    def list(self):
#        response = self.api.list(self.endpoint)
#        index = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]
#        data = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]["ASSET_GROUP_LIST"][
#            "ASSET_GROUP"
#        ]
#        return self.api.parse_response(index=index, data=data)
