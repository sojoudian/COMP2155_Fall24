import napalm

# Initialize the NAPALM driver for Cisco IOS
driver = napalm.get_network_driver("ios")
device = driver(
    hostname="10.0.0.22",
    username="u1",
    password="cisco",
    optional_args={"port": 22, "secret": "cisco"}
)

try:
    # Open a connection to the device
    device.open()
    
    # Retrieve the configured NTP servers
    ntp_servers = device.get_ntp_servers()
    # print(ntp_servers)    
    # Check if the desired NTP server is configured
    desired_ntp_server = '129.6.15.28'
    if desired_ntp_server in ntp_servers:
        print(f"NTP server {desired_ntp_server} is configured correctly.")
    else:
        print(f"NTP server {desired_ntp_server} is NOT configured.")
        print("Currently configured NTP servers:")
        for server in ntp_servers:
            print(f" - {server}")

finally:
    # Close the connection to the device
    device.close()
