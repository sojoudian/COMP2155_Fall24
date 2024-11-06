from netmiko import ConnectHandler

connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

from netmiko import ConnectHandler

with ConnectHandler(**connection) as conn:
    conn.enable()
    conn.config_mode()
    conn.send_config_set(["ip route 0.0.0.0 0.0.0.0 192.168.122.1"])
    print(conn.send_command("show running-config | include ip route"))
    print(conn.send_command("ping 8.8.8.8"))
