import napalm

driver = napalm.get_network_driver("ios")
device = driver(hostname="10.0.0.22", username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})

try:
    device.open()
    interfaces = device.get_interfaces()
    print("Interfaces:")
    for interface, details in interfaces.items():
        print(f"\nInterface: {interface}")
        for key, value in details.items():
            print(f"  {key.capitalize()}: {value}")
finally:
    device.close()

