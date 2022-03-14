from pyqualys.core.endpoint import Endpoint


class Asset(object):
    def __init__(self, api):
        self.group = AssetGroup(api)
        self.host = AssetHost(api)


class AssetHost(Endpoint):
    def __init__(self, api):
        self.api = api
        self.endpoint = "/api/2.0/fo/asset/host/"

    def list(self):
        response = self.api.list(self.endpoint)
        index = response["HOST_LIST_OUTPUT"]["RESPONSE"]
        data = response["HOST_LIST_OUTPUT"]["RESPONSE"]["HOST_LIST"]["HOST"]
        return self.api.parse_response(index=index, data=data)


class AssetGroup(Endpoint):
    def __init__(self, api):
        self.api = api
        self.endpoint = "/api/2.0/fo/asset/group/"

    def list(self):
        response = self.api.list(self.endpoint)
        index = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]
        data = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]["ASSET_GROUP_LIST"][
            "ASSET_GROUP"
        ]
        return self.api.parse_response(index=index, data=data)
