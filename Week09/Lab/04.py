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

# Check CPU usage
cpu_usage = net_connect.send_command("show processes cpu | include CPU")
print("CPU Usage:", cpu_usage)

# Check memory usage
memory_usage = net_connect.send_command("show memory statistics | include Processor")
print("Memory Usage:", memory_usage)

# Disconnect from the device
net_connect.disconnect()