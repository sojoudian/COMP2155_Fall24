# Step 1: First, we must import the ConnectHandler factory function from  Netmiko.

from netmiko import ConnectHandler

# Step 2: This factory function selects the correct Netmiko class based upon the  device_type,
# based on the information we will provide in the Step 2.
# Define the device information
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Replace with the IP address of your Cisco router
    'username': 'your_username',
    'password': 'your_password',
}
net_connect = ConnectHandler(**cisco_device)
