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

# Establish an SSH connection
try:
    connection = ConnectHandler(**cisco_device)
    
    # Execute the command and capture the output
    output = connection.send_command("show ip int brief")
    
    # Print the output
    print("Output of 'show ip int brief':\n", output)
    
finally:
    # Ensure the connection is closed
    connection.disconnect()
