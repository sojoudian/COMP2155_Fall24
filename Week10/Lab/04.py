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
    conn.send_config_from_file('config_script.txt')
    
    output_intIP = conn.send_command("show ip int brief")
    print("Device Interfaces and IP Addresses Information:\n")
    print(output_intIP)

