from pyqualys.core.endpoint import Endpoint


class Asset(object):
    def __init__(self, api):
        self.excluded_ip = Endpoint(api, '/asset/excluded_ip', 'ip', 'ip_set')
        self.excluded_ip.history = Endpoint(api, '/asset/excluded_ip/history', 'history')
        self.group = Endpoint(api, "/asset/group", 'asset_group')
        self.host = Endpoint(api, "/asset/host", 'host')
        self.host.vm = Endpoint(api, '/asset/host/vm')
        self.host.vm.detection = Endpoint(api, '/asset/host/vm/detection', 'host_list_vm_detection', 'host')
        self.ip = Endpoint(api, '/asset/ip', 'ip', 'ip_set')
        self.patch = Endpoint(api, '/asset/patch/index.php')
        self.vhost = Endpoint(api, '/asset/vhost', 'virtual_host')

class Setup(object):
    def __init__(self, api):
        self.restricted_ips = Endpoint(api, '/setup/restricted_ips', 'restricted_ips', 'ip_set')

