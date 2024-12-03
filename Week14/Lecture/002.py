from threading import Thread, Semaphore, current_thread
from time import sleep

# Create our own class Railway
class Railway:
    # Constructor that accepts the number of available berths
    def __init__(self, available):
        self.available = available
        # Create a Semaphore lock
        self.l = Semaphore()

    # A method that reserves a berth
    def reserve(self, wanted):
        # Lock the current object
        self.l.acquire()

        # Display the number of available berths
        print("Available no. of berths = ", self.available)

        # If available >= wanted, allot the berth
        if self.available >= wanted:
            # Find the thread name
            name = current_thread().name

            # Display that the berth is allotted for the person
            print("%d berth(s) are allotted for %s" % (wanted, name))

            # Make a time delay so that the ticket is printed
            sleep(1.5)

            # Decrease the number of available berths
            self.available -= wanted
        else:
            # If available < wanted, then say sorry
            print("Sorry, no berths to allot")

        # Task is completed, release the lock
        self.l.release()

# Create an instance of the Railway class, specifying only one berth is available
obj = Railway(1)

# Create two threads with names specified
t1 = Thread(target=obj.reserve, args=(1,), name="First Person")
t2 = Thread(target=obj.reserve, args=(1,), name="Second Person")

# Start running the threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

