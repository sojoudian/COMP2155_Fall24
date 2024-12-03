# Deadlock example using threads
from threading import Lock, Thread

# Initialize two locks
l1 = Lock()
l2 = Lock()

# Function to simulate ticket cancellation
def cancelticket():
    with l2:  # Acquire lock l2
        print("Cancelticket locked compartment")
        print("Cancelticket wants to lock on train")
        with l1:  # Acquire lock l1
            print("Cancelticket locked train")
    print("Cancellation of ticket is done...")

# Function to simulate ticket booking
def bookticket():
    with l1:  # Acquire lock l1
        print("Bookticket locked train")
        print("Bookticket wants to lock on compartment")
        with l2:  # Acquire lock l2
            print("Bookticket locked compartment")
    print("Booking ticket done...")

# Create two threads
t1 = Thread(target=bookticket, name="BookingThread")
t2 = Thread(target=cancelticket, name="CancellationThread")

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both operations completed.")

