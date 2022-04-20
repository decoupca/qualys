from pprint import pprint
from netdev import config
from netdev.netbox import nb
import qualys
import ipdb
import subprocess
from tqdm.contrib.concurrent import thread_map
from pandas import DataFrame

THREADS = 20

qualys = qualys.api(
    config.QUALYS_USERNAME, config.QUALYS_PASSWORD, config.QUALYS_SERVER
)


def get_nb_by_ip(ip):
    for dev in lb_devices:
        if ip == dev.primary_ip4.address.split("/")[0]:
            return dev
    for vm in lb_vms:
        if ip == vm.primary_ip4.address.split("/")[0]:
            return vm


def get_ptr(ip):
    cmd = f"dig -x {ip} +short"
    result = subprocess.run(cmd.split(" "), capture_output=True)
    if result.returncode == 0:
        record = result.stdout.decode("utf-8").splitlines()
        if record:
            return record[0]
    else:
        return None


def is_reachable(ip):
    cmd = f"ping -c1 -t3 {ip}"
    result = subprocess.run(cmd.split(" "), capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


def get_qualys_info(ip):
    return {"hostname": get_ptr(ip), "ip": ip, "reachable": is_reachable(ip)}


def get_nb_info(device):
    ip = device.primary_ip4.address.split("/")[0]
    return {
        "hostname": device.name,
        "ip": ip,
        "reachable": is_reachable(ip),
        "url": device.url.replace("/api", ""),
    }


# maps Netbox role to Qualys asset group ID
asset_group_ids = {
    "load-balancer": 7539714,
}
lb_nb_devices = nb.dcim.devices.filter(
    role="load-balancer", status="active", has_primary_ip=True
)
lb_devices = [x for x in lb_nb_devices]
lb_device_ips = [x.primary_ip4.address.split("/")[0] for x in lb_devices]

lb_nb_vms = nb.virtualization.virtual_machines.filter(
    role="load-balancer", status="active", has_primary_ip=True
)
lb_vms = [x for x in lb_nb_vms]
lb_vm_ips = [x.primary_ip4.address.split("/")[0] for x in lb_vms]

nb_ips = lb_device_ips + lb_vm_ips


def main():

    group_id = asset_group_ids["load-balancer"]
    response = qualys.asset.group.list(ids=group_id)
    qualys_ips = response["data"]["ASSET_GROUP"]["IP_SET"]["IP"]

    nb_not_in_qualys = []
    qualys_not_in_nb = []

    for ip in nb_ips:
        if ip not in qualys_ips:
            nb_not_in_qualys.append(get_nb_by_ip(ip))

    for ip in qualys_ips:
        if ip not in nb_ips:
            qualys_not_in_nb.append(ip)

    nb_report = thread_map(get_nb_info, nb_not_in_qualys, max_workers=THREADS)
    qualys_report = thread_map(get_qualys_info, qualys_not_in_nb, max_workers=THREADS)

    df1 = DataFrame(nb_report)
    df2 = DataFrame(qualys_report)

    df1.to_csv("nb_report.csv", index=False)
    df2.to_csv("qualys_report.csv", index=False)

    # response = qualys.asset.group.update(id=group_id, set_ips=ips)
    # pprint(response)

    ipdb.set_trace()


if __name__ == "__main__":
    main()
