ciscoDevices = {
    "router_1": {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "device_type": "cisco_ios",
        "username": "admin",
        "password": "password"
    },
    "switch_1": {
        "hostname": "S1",
        "ip_address": "192.168.1.2",
        "device_type": "cisco_ios",
        "username": "admin",
        "password": "SwitchPassword"
    },
    "firewall_1": {
        "hostname": "FW1",
        "ip_address": "192.168.1.3",
        "device_type": "cisco_asa",
        "username": "admin",
        "password": "FWPassword"
    }
}
# print(ciscoDevices)
print("Details about R1: ", ciscoDevices["router_1"])