from netmiko import ConnectHandler

connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

with ConnectHandler(**connection) as conn:
    conn.enable()
    conn.config_mode()
    conn.send_config_set(["ntp server 129.6.15.28"])
