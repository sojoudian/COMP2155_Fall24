import napalm

driver = napalm.get_network_driver("ios")
device = driver(hostname="10.0.0.22", username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})

device.open()
users = device.get_users()
print(f"Device Users:\n {users}")
device.close()
