import napalm

driver = napalm.get_network_driver('ios')
device = driver(hostname="192.168.122.100", username='u1', password='cisco', optional_args={"port":22, "secret": "cisco"})

device.open()
device.close()

