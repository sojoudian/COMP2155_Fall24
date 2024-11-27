## Parallel Pings
from threading import Thread
import os

def ping_device(ip):
    response = os.system(f"ping -c 1 {ip}")
    status = "reachable" if response == 0 else "unreachable"
    print(f"{ip} is {status}")

ips = ["192.168.122.10", "192.168.122.20", "192.168.122.30"]
threads = []

for ip in ips:
    thread = Thread(target=ping_device, args=(ip,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

