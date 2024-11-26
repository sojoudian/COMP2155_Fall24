from threading import *

# Create a function
def display():
    print("Hello I am running")

# Create a thread and run the function 5 times
for i in range(5):
    # Create the thread and specify the function as its target
    t = Thread(target=display)
    # Run the thread
    t.start()

