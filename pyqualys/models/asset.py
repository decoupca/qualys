from pyqualys.endpoints.asset.group import AssetGroup

class Asset(object):
    def __init__(self, api):
        self.group = AssetGroup(api)
