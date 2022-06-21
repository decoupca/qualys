import requests
import xmltodict
from qualys.core.api import API
from qualys.core.groups import Asset, Setup


class api(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.api = API(username, password, hostname)
        self.asset = Asset(self.api)
        self.setup = Setup(self.api)

__all__ = [
    api
]