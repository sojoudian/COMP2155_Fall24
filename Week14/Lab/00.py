from netmiko import ConnectHandler
from threading import Thread, Lock, current_thread

lock = Lock()
devices = [
    {"host": "192.168.122.10", "username": "u1", "password": "cisco", "device_type": "cisco_ios"},
    {"host": "192.168.122.20", "username": "u1", "password": "cisco", "device_type": "cisco_ios"},
    {"host": "192.168.122.30", "username": "u1", "password": "cisco", "device_type": "cisco_ios"},
]

def check_connectivity(device):
    with lock:
        try:
            connection = ConnectHandler(**device)
            print(f"{current_thread().name}: Connected to {device['host']}")
            connection.disconnect()
        except Exception as e:
            print(f"{current_thread().name}: Failed to connect to {device['host']}: {e}")

threads = []
for device in devices:
    thread = Thread(target=check_connectivity, args=(device,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

