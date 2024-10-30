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

output_intIP = net_connect.send_command("show ip int brief")
print("Device Interfaces and IP Addresses Information:\n")
print(output_intIP)

with open("device_interface_ip_info.txt", "w") as file:
    file.write(output_intIP)
print("The device interface ip information was successfully saved in device_interface_ip_info.txt")


# Disconnect from the device
net_connect.disconnect()