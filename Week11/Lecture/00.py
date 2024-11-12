import napalm

driver = napalm.get_network_driver('ios')
device = driver("10.0.0.22", username='u1', password='cisco', optional_args={"port":22, "secret": "cisco"})

device.open()
device.close()

