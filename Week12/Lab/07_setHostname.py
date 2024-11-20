import napalm, sys
driver = napalm.get_network_driver("ios")
device = driver(hostname="192.168.122.100", username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})
try:
    device.open()
    netmiko_conn = device.device
    netmiko_conn.config_mode()
    setHostname = "hostname GBC_CoreRouter"
    netmiko_conn.send_command(setHostname)
    netmiko_conn.exit_config_mode()
    print("hostname has been applied!")
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
finally:
    # Close the connection to the device
