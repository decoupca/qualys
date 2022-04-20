from pprint import pprint
from netdev import config
import qualys
import ipdb

qualys = qualys.api(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)

result = qualys.asset.group.list()
pprint(result)
