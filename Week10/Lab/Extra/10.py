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
    commands = [
        "access-list 10 permit 192.168.1.0 0.0.0.255",
        "access-list 10 deny any"
    ]
    conn.send_config_set(commands)
