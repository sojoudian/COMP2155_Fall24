# Demonstrating thread synchronization and avoiding deadlock
from threading import Lock, Thread

# Initialize two locks
lock1 = Lock()
lock2 = Lock()

# Function to simulate ticket cancellation
def cancel_ticket():
    # Acquire locks in consistent order to avoid deadlock
    with lock1:
        print("Cancelticket: Locked train")
        print("Cancelticket: Wants to lock compartment")
        with lock2:
            print("Cancelticket: Locked compartment")
    print("Cancelticket: Cancellation is done.")

# Function to simulate ticket booking
def book_ticket():
    # Acquire locks in consistent order to avoid deadlock
    with lock1:
        print("Bookticket: Locked train")
        print("Bookticket: Wants to lock compartment")
        with lock2:
            print("Bookticket: Locked compartment")
    print("Bookticket: Booking is done.")

# Create two threads for booking and canceling tickets
thread1 = Thread(target=book_ticket, name="BookingThread")
thread2 = Thread(target=cancel_ticket, name="CancellationThread")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both operations completed successfully.")

