import logging
from netmiko import ConnectHandler

# Set up logging to output to a file with DEBUG level
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Define device connection details
connection = {
    'host': '192.168.122.10',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',  # Enable password
    'device_type': 'cisco_ios'
}

# Establish the connection using ConnectHandler in a context manager
with ConnectHandler(**connection) as conn:
    logger.info("Connection established successfully.")

    # Enter enable mode
    conn.enable()
    logger.info("Entered enable mode.")

    # Enter global config mode and send configuration commands
    conn.config_mode()
    conn.send_config_set([
        "interface GigabitEthernet0/1",
        "description Link to Router",
        "ip address 192.168.140.1 255.255.255.0",
        "no shutdown"
    ])
    logger.info("Configuration commands sent successfully.")

    # Add a static route
    conn.send_config_set(["ip route 0.0.0.0 0.0.0.0 192.168.122.1"])
    logger.info("Static route added successfully.")

    # Display the routing configuration
    route_output = conn.send_command("show running-config | include ip route")
    logger.debug(f"Routing configuration:\n{route_output}")

    # Execute a ping command
    ping_output = conn.send_command("ping 8.8.8.8")
    logger.debug(f"Ping output:\n{ping_output}")

    # Save the configuration
    conn.save_config()
    logger.info("Configuration saved successfully.")

logger.info("Disconnected from device.")