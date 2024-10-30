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

# Retrieve the device version information
version_info = net_connect.send_command("show version")

# Save the version information to a file
with open("device_version_info.txt", "w") as backup_file:
    backup_file.write(version_info)
print("Device version information backed up to device_version_info.txt")

# Disconnect from the device
net_connect.disconnect()