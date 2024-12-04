# DEAD LOCK
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
    """Simulates a deadlock by acquiring locks in different orders."""
    print(f"{current_thread().name}: Trying to acquire semaphore for {device['host']}...")
    with semaphore:
        print(f"{current_thread().name}: Semaphore acquired for {device['host']}")

        # Simulate work before acquiring file lock
        time.sleep(1)

        print(f"{current_thread().name}: Trying to acquire file lock for {device['host']}...")
        file_lock.acquire()  # Intentionally hold file lock while semaphore is still held
        try:
            # Simulate configuration backup
            print(f"{current_thread().name}: Backing up configuration for {device['host']}...")
            time.sleep(2)  # Simulate delay in backup process
        finally:
            print(f"{current_thread().name}: Releasing file lock for {device['host']}")
            file_lock.release()

    # This part creates the deadlock: Threads will now try to acquire locks in reverse order
    print(f"{current_thread().name}: Trying to acquire semaphore again for {device['host']}...")
    semaphore.acquire()  # Attempt to reacquire the semaphore, creating a dependency loop
    try:
        print(f"{current_thread().name}: Re-acquired semaphore for {device['host']}")
    finally:
        print(f"{current_thread().name}: Releasing semaphore for {device['host']}")
        semaphore.release()

# Create threads for each device
threads = []
for device in devices:
    thread = Thread(target=backup_device_config, args=(device,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All device configurations have been processed!")
