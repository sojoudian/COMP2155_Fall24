import logging
from netmiko import Netmiko

# Set up logging to output to a file with DEBUG level
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Define device connection details
connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'device_type': 'cisco_ios',
    'secret': 'enable_secret'  # Replace with your actual enable password
}

# Establish the connection
net_connect = Netmiko(**connection)
logger.info("Connection established successfully.")

# Enter enable mode
net_connect.enable()
logger.info("Entered enable mode.")

# Execute a command
output = net_connect.send_command("show ip interface brief")
logger.debug(f"Command output:\n{output}")

# Send a configuration set
config_commands = [
    "interface GigabitEthernet0/1",
    "description Link to Router",
    "ip address 192.168.1.1 255.255.255.0",
    "no shutdown"
]
net_connect.send_config_set(config_commands)
logger.info("Configuration commands sent successfully.")

# Save configuration
net_connect.save_config()
logger.info("Configuration saved successfully.")

# Disconnect from the device
net_connect.disconnect()
logger.info("Disconnected from device.")
