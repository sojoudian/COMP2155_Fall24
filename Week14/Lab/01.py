from netmiko import ConnectHandler
from threading import Thread, Semaphore, current_thread
import time

# Define the semaphore to limit concurrent SSH connections
max_connections = 3  # Adjust this based on your system or device limitations
semaphore = Semaphore(max_connections)

# Device details
devices = [
    {
        "host": "192.168.122.10",
        "username": "u1",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 60,
    },
    {
        "host": "192.168.122.20",
        "username": "u1",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 60,
    },
    {
        "host": "192.168.122.30",
        "username": "u1",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 60,
    },
]

def backup_device_config(device):
    """Backup the running configuration of a network device."""
    with semaphore:  # Acquire a semaphore slot
        print(f"{current_thread().name}: Semaphore acquired for {device['host']}")
        try:
            # Connect to the device
            connection = ConnectHandler(**device)
            connection.enable()  # Enter privileged mode

            # Retrieve the running configuration
            print(f"{current_thread().name}: Retrieving configuration from {device['host']}...")
            running_config = connection.send_command("show running-config")
            
            # Simulate delay for demonstration purposes
            time.sleep(2)

            # Save the configuration to a local file
            filename = f"backup_{device['host']}.txt"
            with open(filename, "w") as backup_file:
                backup_file.write(running_config)
            print(f"{current_thread().name}: Backup saved to {filename}")

            # Disconnect from the device
            connection.disconnect()

        except Exception as e:
            print(f"{current_thread().name}: Failed to backup {device['host']}: {e}")
        finally:
            print(f"{current_thread().name}: Semaphore released for {device['host']}")

# Create threads for each device
threads = []
for device in devices:
    thread = Thread(target=backup_device_config, args=(device,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All device configurations have been backed up successfully!")
