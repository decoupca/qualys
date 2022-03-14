class AssetGroup(object):
    def __init__(self, api):
        self.api = api
        self.endpoint = "/api/2.0/fo/asset/group/"


    def add(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, action="add", data=data)
        return self.api.parse_response(response)

    def delete(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, action="delete", data=data)
        return self.api.parse_response(response)

    def list(self):
        response = self.api.call(self.endpoint, action="list")
        index = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]
        data = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]['ASSET_GROUP_LIST']['ASSET_GROUP']
        return self.api.parse_response(index=index, data=data)

    def update(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, data=data, action="edit")
        return self.api.parse_response(response)
