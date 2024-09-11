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
#print(ciscoDevices)
#print("Details about R1: ", ciscoDevices["router_1"])


# Accessing device information
for device, info in ciscoDevices.items():
    print(f"Device: {device}")
    print(f"Hostname: {info['hostname']} ")
    print(f"IP Address: {info['ip_address']} ")
    print(f"Device Type: {info['device_type']} ")
    print("------------------------------------------")






