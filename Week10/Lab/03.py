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
        "interface Ethernet0/2",
        "ip address 192.168.1.1 255.255.255.0",
        "no shutdown"
    ]
    conn.send_config_set(commands)
    # Make sure the changes were correct:
    output_intIP = conn.send_command("show ip int brief")
    print("Device Interfaces and IP Addresses Information:\n")
    print(output_intIP)
