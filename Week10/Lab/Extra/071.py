import logging
import time
from netmiko import Netmiko

# Set up logging to output to a file with DEBUG level
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Define device connection details
connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'device_type': 'cisco_ios'
}

# Establish the connection
net_connect = Netmiko(**connection)
logger.info("Connection established successfully.")

# Manually write to the channel to execute the command
net_connect.write_channel("show ip interface brief\n")
logger.info("Command 'show ip interface brief' sent to device.")

# Wait briefly to ensure the command is executed and the output is ready
time.sleep(1)

# Read the output from the device
output = net_connect.read_channel()
logger.debug(f"Command output:\n{output}")

# Disconnect from the device
net_connect.disconnect()
logger.info("Disconnected from device.")
