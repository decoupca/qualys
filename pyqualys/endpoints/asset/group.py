class AssetGroup(object):
    def __init__(self, api):
        self.api = api
        self.endpoint = "/api/2.0/fo/asset/group/"

    def list(self):
        response = self.api.call(self.endpoint, action="list")
        index = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]
        data = response["ASSET_GROUP_LIST_OUTPUT"]["RESPONSE"]['ASSET_GROUP_LIST']['ASSET_GROUP']
        return self.api.parse_response(index=index, data=data)

    def update(
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
        data = {
            "id": group_id,
            "add_appliance_ids": add_appliance_ids,
            "add_dns_names": add_dns_names,
            "add_ips": add_ips,
            "add_netbios_names": add_netbios_names,
            "cvss_enviro_ar": cvss_enviro_ar,
            "cvss_enviro_cdp": cvss_enviro_cdp,
            "cvss_enviro_cr": cvss_enviro_cr,
            "cvss_enviro_ir": cvss_enviro_ir,
            "cvss_enviro_td": cvss_enviro_td,
            "default_appliance_id": default_appliance_id,
            "remove_appliance_ids": remove_appliance_ids,
            "remove_dns_names": remove_dns_names,
            "remove_ips": remove_ips,
            "remove_netbios_names": remove_netbios_names,
            "set_appliance_ids": set_appliance_ids,
            "set_business_impact": business_impact.capitalize(),
            "set_comments": comments,
            "set_divison": division,
            "set_dns_names": set_dns_names,
            "set_function": function,
            "set_ips": set_ips,
            "set_location": location,
            "set_netbios_names": set_netbios_names,
            "set_title": title,
        }
        response = self.api.call(self.endpoint, data=data, action="edit")
        return self.api.parse_response(response)
