from threading import Thread
from netmiko import ConnectHandler

def push_config(ip, hostname):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "u1",
        "password": "cisco",
        "secret": "cisco",
    }
    commands = [
        f"hostname {hostname}"
    ]
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        connection.send_config_set(commands)
        print(f"Hostname set to {hostname} on {ip}")
    finally:
        connection.disconnect()

# Mapping IPs to hostnames
ip_to_hostname = {
    "192.168.122.10": "TorontoCoreRouter",
    "192.168.122.20": "VancouverCoreRouter",
    "192.168.122.30": "MontrealCoreRouter",
}

threads = []

for ip, hostname in ip_to_hostname.items():
    thread = Thread(target=push_config, args=(ip, hostname))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
