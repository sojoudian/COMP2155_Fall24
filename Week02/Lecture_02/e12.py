import os
import platform

def ping_device(ip_address):
    # Check if the system is Windows or not:
    param = '-n' if platform.system().lower() == 'windows' else '-c' # using the platform package
    response = os.system(f'ping {param} 1 {ip_address}') # using the OS package

    if response == 0:
        print(f'Device {ip_address} is reachable')
    else:
        print(f'Device {ip_address} is not reachable')

ip = "127.0.0.1"
ping_device(ip)
