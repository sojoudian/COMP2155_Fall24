import napalm

# Replace with your device's details
driver = napalm.get_network_driver('ios')  # Adjust 'ios' based on your device's OS
device = driver(
    hostname='10.0.0.22',
    username='u1',
    password='cisco',
    optional_args={"port": 22, "secret": "cisco"}
)

try:
    # Open a connection to the device
    device.open()

    # Retrieve device facts
    facts = device.get_facts()
    current_hostname = facts.get('hostname', 'Unknown')

    print(f"Current hostname: {current_hostname}")

finally:
    # Close the connection
    device.close()
