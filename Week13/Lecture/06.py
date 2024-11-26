# Step-1: Create an independent class
class MyThread:
    def __init__(self, message):
        self.message = message

    def display(self, x, y):
        print(f"{self.message}, Arguments: {x}, {y}")

# Step-2: Create an object of MyThread class
obj = MyThread("Hello")

# Step-3: Create a thread by passing the object's method as the target
from threading import Thread
t1 = Thread(target=obj.display, args=(1, 2))

# Start the thread
t1.start()

# Wait till the thread completes
t1.join()

