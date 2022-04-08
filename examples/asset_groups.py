from pprint import pprint
from netdev import config
from netdev.netbox import nb
import pyqualys
import ipdb

qualys = pyqualys.Qualys(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)

ios_hosts = nb.dcim.devices.filter(platform="ios", status="active", has_primary_ip=True)
ips = [x.primary_ip4.address.split("/")[0] for x in ios_hosts]


group_id = "12249485"
# host_list = qualys.asset.host.list()
# vhost_list = qualys.asset.vhost.list()
# det = qualys.asset.host.vm.detection.list()
response = qualys.asset.group.update(
    id=group_id,
    set_ips=ips,
    # set_comments="All IOS hosts updated from NetBox",
    # set_business_impact="Low",
    # set_title='Python is awesome',
)
pprint(response)
