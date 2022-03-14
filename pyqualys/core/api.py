import requests
import xmltodict

class API(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.auth = (self.username, self.password)
        self.headers = {
            "X-Requested-With": "pyqualys",
        }

    def build_url(self, endpoint, action=None):
        url = f"https://{self.hostname}/{endpoint}"
        if action:
            url = f"{url}?action={action}"
        return url

    def parse_args(self, args):
        # concatenate lists
        for k, v in args.items():
            if isinstance(v, list):
                args[k] = ','.join(v)
        return args

    def parse_response(self, response=None, index=None, data=None):
        if index is None:
            index = response["SIMPLE_RETURN"]["RESPONSE"]
        timestamp = index.get("DATETIME")
        # if no code in response, treat as success (0)
        code = index.get("CODE", 0)
        msg = index.get("TEXT")
        result = {
            "timestamp": timestamp,
            "code": code,
            "msg": msg,
            "data": data,
        }
        if code:
            code = int(code)
            # https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf
            # p. 750
            if code > 999:
                raise ValueError(f"Error {code}: {msg}")
        else:
            return result

    def get(self, url):
        return requests.get(url, auth=self.auth, headers=self.headers)

    def post(self, url, data):
        return requests.post(url, data=data, auth=self.auth, headers=self.headers)

    def call(self, endpoint, data=None, action=None):
        url = self.build_url(endpoint, action)
        if action == 'list':
            response = self.get(url)
        else:
            response = self.post(url, data)
        return xmltodict.parse(response.content)
