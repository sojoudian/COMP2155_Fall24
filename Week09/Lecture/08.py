# Step 1: Import the ConnectHandler factory function from Netmiko.
from netmiko import ConnectHandler

# Step 2: Define the device information
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',  # Replace with the IP address of your Cisco router
    'username': 'u1',
    'password': 'cisco',
}

# Step 3: Establish an SSH connection
net_connect = ConnectHandler(**cisco_device)

# Step 4: Retrieve the device prompt
# find_prompt(): This method retrieves the device prompt, which can help verify the connection.
prompt_text = net_connect.find_prompt()
print(f"Device prompt: {prompt_text}")

# Step 5: Run the 'show version' command and capture the output
# send_command("show version"): Sends the command to the device and captures the output.
output = net_connect.send_command("show version")
print("Output of 'show version':\n", output)

# Optional: Disconnect after commands are executed
net_connect.disconnect()
