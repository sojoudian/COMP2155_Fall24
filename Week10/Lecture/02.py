from netmiko import Netmiko

net_connect = Netmiko(host='127.0.0.1', username='student', password='student', device_type='linux')

print(net_connect.find_prompt())

net_connect.disconnect()
