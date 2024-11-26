# Creating our own thread
from threading import Thread

# Create a class as a subclass to the Thread class
class MyThread(Thread):
    # Override the run() method of the Thread class
    def run(self):
        for i in range(1, 6):
            print(i)

# Create an instance of MyThread class
t1 = MyThread()

# Start running the thread t1
t1.start()

# Wait till the thread completes its job
t1.join()

