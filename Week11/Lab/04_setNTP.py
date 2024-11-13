import napalm
from netmiko import Netmiko

# Set up NAPALM device connection
driver = napalm.get_network_driver("ios")
device = driver(
    hostname="10.0.0.22",
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

    # Send the NTP server configuration command
    ntp_command = "ntp server 129.6.15.28"
    netmiko_conn.send_command(ntp_command)

    # Exit configuration mode
    netmiko_conn.exit_config_mode()

    print("NTP server configuration applied successfully.")

finally:
    # Close the connection to the device
    device.close()
