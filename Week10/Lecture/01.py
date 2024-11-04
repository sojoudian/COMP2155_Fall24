from netmiko import Netmiko

net_connect = Netmiko(host='192.168.122.100', username='u1', password='cisco', device_type='cisco_ios')

print(net_connect.find_prompt())

net_connect.disconnect()
