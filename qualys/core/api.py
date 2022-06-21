import requests
import xmltodict
from urllib.parse import urlencode


class API(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.auth = (self.username, self.password)
        self.path = "api/2.0/fo"
        self.headers = {
            "X-Requested-With": "pyqualys",
        }

    def build_url(self, endpoint, query=None):
        url = f"https://{self.hostname}/{self.path}{endpoint}/"
        if query:
            url = f"{url}?{urlencode(query)}"
        return url

    def parse_args(self, args):
        # concatenate lists
        for k, v in args.items():
            if isinstance(v, list):
                args[k] = ",".join(v)
        return args

    def parse_response(self, response, index_key=None, data_key=None, raw=False):
        if raw:
            return response
        if index_key:
            index_key = index_key.upper()
            key = f"{index_key}_LIST_OUTPUT"
            index = response[key]["RESPONSE"]
            if data_key:
                data = index.get(data_key.upper())
            else:
                data = index.get(f"{index_key}_LIST")
        else:
            index = response["SIMPLE_RETURN"]["RESPONSE"]
            data = None

        timestamp = index.get("DATETIME")
        # if no code in response, treat as success (0)
        code = index.get("CODE", 0)
        warning = index.get("WARNING")
        if warning:
            code = warning["CODE"]
            msg = warning["TEXT"]
            url = warning["URL"]
        else:
            msg = index.get("TEXT")
            url = None
        result = {
            "timestamp": timestamp,
            "code": int(code),
            "msg": msg,
            "data": data,
            "url": url,
        }
        if result["code"]:
            code = result["code"]
            # https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf
            # p. 750
            if code > 999:
                if code != 1980:
                    # Code 1980 is paginated results
                    raise ValueError(f"Error {code}: {msg}")
        return result

    def get(self, url):
        return requests.get(url, auth=self.auth, headers=self.headers)

    def post(self, url, data):
        return requests.post(url, data=data, auth=self.auth, headers=self.headers)

    def call(self, endpoint, data=None, action=None):
        if action is not None:
            query = {"action": action}
        else:
            query = {}
        url = self.build_url(endpoint, query)
        if action == "list":
            if data:
                query.update(data)
            response = self.get(url)
        else:
            response = self.post(url, data)
        return xmltodict.parse(response.content)
