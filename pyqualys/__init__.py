import requests
import xmltodict
import ipdb
from pyqualys.core.api import API
from pyqualys.core.groups import Asset, Setup


class Qualys(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.api = API(username, password, hostname)
        self.asset = Asset(self.api)
        self.setup = Setup(self.api)
