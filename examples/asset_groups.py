from pprint import pprint
from netdev import config
from netdev.netbox import nb
import pyqualys


qualys = pyqualys.Qualys(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)

ios_hosts = nb.dcim.devices.filter(platform="ios", status="active", has_primary_ip=True)
ips = []
for host in ios_hosts:
    ips.append(host.primary_ip4.address.split("/")[0])


group_id = "12249485"
#pprint(qualys.asset.group.list())
response = qualys.asset.group.update(
    group_id=group_id,
    set_ips=ips,
    comments="All IOS hosts updated from NetBox",
    business_impact="High",
)
pprint(response)


import ipdb

ipdb.set_trace()
