#Get Running Configuration and Compare with Startup
# 
import napalm

driver = napalm.get_network_driver("ios")
device = driver(hostname="10.0.0.22", username="u1", password="cisco", optional_args={"port": 22, "secret": "cisco"})

device.open()
running_config = device.get_config()["running"]
startup_config = device.get_config()["startup"]

if running_config == startup_config:
    print("Running and startup configurations match.")
else:
    print("Running and startup configurations do not match.")

device.close()
