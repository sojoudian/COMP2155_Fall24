from netmiko import ConnectHandler

# Define the Cisco device
device = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',  # Replace with your device IP
    'username': 'u1',
    'password': 'cisco',
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Retrieve the current date and time
clock_info = net_connect.send_command("show clock")
print("Device Clock Information:", clock_info)

# Save the clock information to a file
with open("device_clock.txt", "w") as file:
    file.write(clock_info)
print("Clock information saved to device_clock.txt")

# Disconnect from the device
net_connect.disconnect()