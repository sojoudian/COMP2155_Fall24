import napalm

driver = napalm.get_network_driver("ios")
device = driver(hostname="10.0.0.22", username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})


device.open()
interfaces = device.get_interfaces()
print("Interfaces:", interfaces)
device.close()


