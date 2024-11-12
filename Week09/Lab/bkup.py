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
# Format the CPU output for better readability
cpu_lines = cpu_usage.strip().split("\n")
cpu_output = "\n".join(f"CPU Usage at {line.split()[-1]}: {line.split()[-4]}%" for line in cpu_lines)
print("Formatted CPU Usage:\n", cpu_output)

# Check memory usage
memory_usage = net_connect.send_command("show memory statistics | include Processor")
# Format the memory output for better readability
memory_lines = memory_usage.strip().split("\n")
formatted_memory = "\n".join(f"Processor Memory: {line.split()[3]} used out of {line.split()[1]}" for line in memory_lines)
print("Formatted Memory Usage:\n", formatted_memory)

# Disconnect from the device
net_connect.disconnect()