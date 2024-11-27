from threading import Thread
import napalm

def backup_config(ip):
    driver = napalm.get_network_driver("ios")
    device = driver(hostname=ip, username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})
    try:
        device.open()
        config = device.get_config()["running"]
        with open(f"{ip}_running_config.txt", "w") as file:
            file.write(config)
        print(f"Backup saved for {ip}")
    finally:
        device.close()

ips = ["192.168.122.10", "192.168.122.20", "192.168.122.30"]
threads = []

for ip in ips:
    thread = Thread(target=backup_config, args=(ip,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

