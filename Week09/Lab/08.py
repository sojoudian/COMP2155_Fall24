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
memory_usage = net_connect.send_command("show memory statistics")
# Format the memory output for better readability
memory_lines = memory_usage.strip().split("\n")

# Look for lines related to Processor memory specifically
for line in memory_lines:
    if "Processor" in line:
        parts = line.split()
        used_memory = parts[3]
        total_memory = parts[1]
        free_memory = parts[5]
        memory_output = (
            f"Processor Memory:\n"
            f"  - Total: {total_memory} KB\n"
            f"  - Used: {used_memory} KB\n"
            f"  - Free: {free_memory} KB"
        )
        print("Formatted Memory Usage:\n", memory_output)

# Disconnect from the device
net_connect.disconnect()