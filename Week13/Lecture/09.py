# Multitasking using two threads
from threading import Thread, current_thread
from time import sleep

# Create our own class
class Railway:
    # Constructor that accepts the number of available berths
    def __init__(self, available):
        self.available = available

    # A method that reserves a berth
    def reserve(self, wanted):
        print("Available no. of berths =", self.available)

        # If available >= wanted, allot the berth
        if self.available >= wanted:
            # Find the thread name
            name = current_thread().name  # Use `name` instead of `getName()`

            # Display the berth is allotted for the person
            print("%d berths are allotted for %s" % (wanted, name))

            # Make time delay so that the ticket is printed
            sleep(1.5)

            # Decrease the number of available berths
            self.available -= wanted
        else:
            # If available < wanted, say sorry
            print("Sorry, no berths to allot")

# Create an instance of the Railway class
# Specify that only one berth is available
obj = Railway(1)

# Create two threads and specify that 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

# Set names for the threads using the `name` attribute
t1.name = "First Person"
t2.name = "Second Person"

# Start running the threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()

