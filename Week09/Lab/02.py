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

# Retrieve the routing table
output = net_connect.send_command("show ip route")
print("Routing Table:\n", output)

# Disconnect from the device
net_connect.disconnect()