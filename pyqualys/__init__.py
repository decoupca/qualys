import requests
import xmltodict
import ipdb
from pyqualys.core.api import API
from pyqualys.models.asset import Asset


class Qualys(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.api = API(username, password, hostname)
        self.asset = Asset(self.api)
