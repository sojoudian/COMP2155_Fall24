import sys

import napalm
from netmiko import Netmiko

# Set up NAPALM device connection
driver = napalm.get_network_driver("ios")
device = driver(
    hostname="192.168.122.100",
    username="u1",
    password="cisco",
    optional_args={"port": 22, "secret": "cisco"}
)

# Open a connection to the device
device.open()

try:
    # Access the underlying Netmiko connection
    netmiko_conn = device.device

    # Enter configuration mode
    netmiko_conn.config_mode()

    # Internet route command
    Internet_command = "ip route 0.0.0.0 0.0.0.0 192.168.122.1"
    netmiko_conn.send_command(Internet_command)

    # Exit configuration mode
    netmiko_conn.exit_config_mode()

    print("Internet route has been applied!")

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)

finally:
    # Close the connection to the device
