from threading import Thread
import napalm

def get_device_facts(ip):
    driver = napalm.get_network_driver("ios")
    device = driver(hostname=ip, username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})
    try:
        device.open()
        facts = device.get_facts()
        print(f"Facts for {ip}:")
        print(facts)
    finally:
        device.close()

ips = ["192.168.122.10", "192.168.122.20", "192.168.122.30"]
threads = []

for ip in ips:
    thread = Thread(target=get_device_facts, args=(ip,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

