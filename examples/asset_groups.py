import pyqualys
from pprint import pprint
from netdev import config

qualys = pyqualys.Qualys(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)

group_id = '12249485'
response = qualys.update_asset_group(group_id=group_id, set_ips="172.16.16.254,10.2.3.4,192.168.1.1")
pprint(response)
#import ipdb; ipdb.set_trace()
