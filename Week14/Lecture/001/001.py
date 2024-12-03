from threading import Thread, Lock, current_thread
from time import sleep

# Define the Railway class
class Railway:
    def __init__(self, available):
        # Initialize the available berths and a lock object
        self.available = available
        self.l = Lock()

    def reserve(self, wanted):
        # Acquire the lock
        self.l.acquire()

        # Display the number of available berths
        print(f"Available no. of berths = {self.available}")

        # Check if the required berths are available
        if self.available >= wanted:
            # Get the name of the current thread
            name = current_thread().name

            # Allocate the berth
            print(f"{wanted} berths are allotted for {name}")

            # Simulate delay for ticket processing
            sleep(1.5)

            # Decrease the number of available berths
            self.available -= wanted
        else:
            # Inform that no berths are available
            print("Sorry, no berths to allot")

        # Release the lock
        self.l.release()

# Create an instance of Railway with 1 available berth
obj = Railway(1)

# Create two threads requesting 1 berth each, passing names directly
t1 = Thread(target=obj.reserve, args=(1,), name="First Person")
t2 = Thread(target=obj.reserve, args=(1,), name="Second Person")

# Start the threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Reservation process completed.")

