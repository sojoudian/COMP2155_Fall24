from netmiko import ConnectHandler

# Define the connection details
connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

# Connect and apply configuration
with ConnectHandler(**connection) as conn:
    conn.enable()  # Enter privileged EXEC mode
    conn.config_mode()  # Enter global configuration mode
    conn.send_config_set(["ntp server 129.6.15.28"])  # Apply NTP configuration

    # Exit config mode and verify the configuration
    conn.exit_config_mode()  # Exit global config mode
    output = conn.send_command("show run | include ntp server")  # Check for NTP server configuration

print("Verification output:\n", output)

