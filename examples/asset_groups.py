from pprint import pprint
from netdev import config
from netdev.netbox import nb
import pyqualys
import ipdb

qualys = pyqualys.Qualys(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)

# maps Netbox role to Qualys asset group ID
asset_group_ids = {
    'load-balancer': 7539714,
}

lb_devices = nb.dcim.devices.filter(role='load-balancer', status="active", has_primary_ip=True)
lb_device_ips = [x.primary_ip4.address.split("/")[0] for x in lb_devices]

lb_vms = nb.virtualization.virtual_machines.filter(role='load-balancer', status='active', has_primary_ip=True)
lb_vm_ips = [x.primary_ip4.address.split("/")[0] for x in lb_vms]

ips = lb_device_ips + lb_vm_ips

group_id = asset_group_ids['load-balancer']
response = qualys.asset.group.list(ids=group_id)
#response = qualys.asset.group.update(id=group_id, set_ips=ips)
#pprint(response)
ipdb.set_trace()
