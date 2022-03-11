import requests
import xmltodict
import ipdb

class Qualys(object):
    def __init__(self, username, password, hostname="qualysapi.qualys.com"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.auth = (self.username, self.password)
        self.headers = {
            "X-Requested-With": "pyqualys",
        }

    def _build_url(self, endpoint):
        return f"https://{self.hostname}/{endpoint}"

    def _parse_response(self, response):
        result = {}
        response = response['SIMPLE_RETURN']['RESPONSE']
        timestamp = response.get('DATETIME')
        code = response.get('CODE')
        msg = response.get('TEXT')
        if timestamp:
            result.update({'timestamp': timestamp})
        if code:
            result.update({'code': int(code)})
        if msg:
            result.update({'msg': msg})
        return result

    def _get(self, endpoint):
        url = self._build_url(endpoint)
        response = requests.get(url, auth=self.auth, headers=self.headers)
        return xmltodict.parse(response.content)

    def _post(self, endpoint, data):
        url = self._build_url(endpoint)
        data = {k: v for k, v in data.items() if v is not None}
        response = requests.post(url, data=data, auth=self.auth, headers=self.headers)
        return xmltodict.parse(response.content)

    def list_asset_groups(self):
        endpoint = "/api/2.0/fo/asset/group/?action=list"
        response = self._get(endpoint)
        return response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]["ASSET_GROUP_LIST"][
            "ASSET_GROUP"
        ]

    def update_asset_group(
        self,
        group_id,
        add_appliance_ids=None,
        add_dns_names=None,
        add_ips=None,
        add_netbios_names=None,
        business_impact=None,
        comments=None,
        cvss_enviro_ar=None,
        cvss_enviro_cdp=None,
        cvss_enviro_cr=None,
        cvss_enviro_ir=None,
        cvss_enviro_td=None,
        default_appliance_id=None,
        division=None,
        function=None,
        location=None,
        remove_appliance_ids=None,
        remove_dns_names=None,
        remove_ips=None,
        remove_netbios_names=None,
        set_appliance_ids=None,
        set_dns_names=None,
        set_ips=None,
        set_netbios_names=None,
        title=None,
    ):
        endpoint = "/api/2.0/fo/asset/group/?action=edit"
        data = {
            'id': group_id,
            'add_appliance_ids': add_appliance_ids,
            'add_dns_names': add_dns_names,
            'add_ips': add_ips,
            'add_netbios_names': add_netbios_names,
            'set_business_impact': business_impact,
            'set_comments': comments,
            'cvss_enviro_ar': cvss_enviro_ar,
            'cvss_enviro_cdp': cvss_enviro_cdp,
            'cvss_enviro_cr': cvss_enviro_cr,
            'cvss_enviro_ir': cvss_enviro_ir,
            'cvss_enviro_td': cvss_enviro_td,
            'default_appliance_id': default_appliance_id,
            'set_divison': division,
            'set_function': function,
            'set_location': location,
            'remove_appliance_ids': remove_appliance_ids,
            'remove_dns_names': remove_dns_names,
            'remove_ips': remove_ips,
            'remove_netbios_names': remove_netbios_names,
            'set_appliance_ids': set_appliance_ids,
            'set_dns_names': set_dns_names,
            'set_ips': set_ips,
            'set_netbios_names': set_netbios_names,
            'set_title': title,
        }
        response = self._post(endpoint, data=data)
        return self._parse_response(response)
