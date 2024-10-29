from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

cisco = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
}

try:
    net_connect = ConnectHandler(**cisco)
    print("Successfully connected to device")
except NetMikoTimeoutException:
    print(f"Timeout error connecting to device {cisco['host']}")
except NetMikoAuthenticationException:
    print(f"Authentication failed for {cisco['host']}")
except Exception as e:
    print(f"Failed to connect to device {cisco['host']}: {str(e)}")
