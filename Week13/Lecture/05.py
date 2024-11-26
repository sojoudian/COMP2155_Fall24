# A thread that accesses the instance variables
from threading import Thread

# Create a class as a subclass to the Thread class
class MyThread(Thread):
    def __init__(self, str):
        Thread.__init__(self)  # Initialize the parent class 
        self.str = str

    # Override the run() method of Thread class
    def run(self):
        print(self.str)

# Create an instance of MyThread class and pass the string
t1 = MyThread("Hello")

# Start running the thread
t1.start()

# Wait till the thread completes its job
t1.join()
