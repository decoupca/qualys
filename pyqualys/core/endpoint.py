class Endpoint(object):
    def __init__(self, api, endpoint, result_key=None, data_key=None):
        self.api = api
        self.endpoint = endpoint
        self.result_key = result_key
        self.data_key = data_key

    def get(self, raw=False, **kwargs):
        return self.api.get(self.endpoint, data=data)

    def add(self, raw=False, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, data=data, action='add')
        return self.api.parse_response(response, raw=raw)

    def delete(self, raw=False, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, data=data, action='delete')
        return self.api.parse_response(response, raw=raw)

    def list(self, raw=False):
        response = self.api.call(self.endpoint, action='list')
        return self.api.parse_response(response, self.result_key, self.data_key, raw=raw)

    def update(self, raw=False, **kwargs):
        data = self.api.parse_args(kwargs)
        response = self.api.call(self.endpoint, data=data, action='edit')
        return self.api.parse_response(response, raw=raw)

