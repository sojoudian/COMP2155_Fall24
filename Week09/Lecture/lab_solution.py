from netmiko import ConnectHandler

# Define the Cisco device
device = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',
    'username': 'u1',
    'password': 'cisco',
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Retrieve and save 'show version'
version_output = net_connect.send_command("show version")
with open("device_version.txt", "w") as file:
    file.write(version_output)
print("Device version saved to device_version.txt")

# Retrieve and save 'show ip interface brief'
interface_output = net_connect.send_command("show ip interface brief")
with open("interface_status.txt", "w") as file:
    file.write(interface_output)
print("Interface status saved to interface_status.txt")

# Retrieve and save 'show arp'
arp_output = net_connect.send_command("show arp")
with open("arp_table.txt", "w") as file:
    file.write(arp_output)
print("ARP table saved to arp_table.txt")

# Disconnect from the device
net_connect.disconnect()
