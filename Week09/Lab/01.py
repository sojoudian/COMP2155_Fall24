from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',
    'username': 'u1',
    'password': 'cisco',
}
net_connect = ConnectHandler(**device)
uptime_output = net_connect.send_command("show version | include uptime")
print("Device Uptime:", uptime_output)
net_connect.disconnect()
