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

# Retrieve the running configuration
running_config = net_connect.send_command("show running-config")

# Save the configuration to a file
with open("backup_config.txt", "w") as backup_file:
    backup_file.write(running_config)
print("Configuration backed up to backup_config.txt")

# Disconnect from the device
net_connect.disconnect()