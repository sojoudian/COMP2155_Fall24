from netmiko import ConnectHandler

connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',    
    'device_type': 'cisco_ios'
}

with ConnectHandler(**connection) as conn:
    conn.enable()  # Enter enable mode
    save_output = conn.save_config()  # Save the current running config to startup config
    print(save_output)
