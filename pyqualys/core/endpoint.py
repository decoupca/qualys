class Endpoint(object):
    def __init__(self, api, endpoint, result_key, data_key=None):
        self.api = api
        self.endpoint = endpoint
        self.result_key = result_key
        self.data_key = data_key

    def add(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.add(self.endpoint, data=data)
        return self.api.parse_response(response)

    def delete(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.update(self.endpoint, data=data)
        return self.api.parse_response(response)

    def list(self):
        response = self.api.list(self.endpoint)
        return self.api.parse_response(response, self.result_key, self.data_key)

    def update(self, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.update(self.endpoint, data=data)
        return self.api.parse_response(response)
