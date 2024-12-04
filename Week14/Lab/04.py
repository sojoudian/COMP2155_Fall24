# FIX THE DEAD LOCK
from netmiko import ConnectHandler
from threading import Thread, Lock, Semaphore, current_thread
import time

# Define a semaphore to limit concurrent connections
semaphore = Semaphore(2)  # Allow only 2 threads at a time

# Define a separate lock for file access
file_lock = Lock()

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
    """Safely backup the running configuration of a network device."""
    # Acquire semaphore first (consistent order)
    print(f"{current_thread().name}: Trying to acquire semaphore for {device['host']}...")
    with semaphore:
        print(f"{current_thread().name}: Semaphore acquired for {device['host']}")
        
        # Acquire file lock after semaphore (consistent order)
        print(f"{current_thread().name}: Trying to acquire file lock for {device['host']}...")
        with file_lock:
            print(f"{current_thread().name}: File lock acquired for {device['host']}")

            try:
                # Connect to the device
                connection = ConnectHandler(**device)
                connection.enable()  # Enter privileged mode

                # Retrieve the running configuration
                print(f"{current_thread().name}: Retrieving configuration from {device['host']}...")
                running_config = connection.send_command("show running-config")
                
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
                print(f"{current_thread().name}: Releasing file lock for {device['host']}")

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

