# Single tasking using a single thread
from threading import Thread
from time import sleep

# Create our own class
class MyThread:
    # A method that performs 3 tasks one by one
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder for 5 mins.........", end="")
        sleep(5)
        print("Done")

    def task2(self):
        print("Add sugar and boil for 3 mins............", end="")
        sleep(3)
        print("Done")

    def task3(self):
        print("Filter and serve............", end="")
        print("Done")

# Create an instance of our class
obj = MyThread()

# Create a thread and run the prepareTea method of obj
t = Thread(target=obj.prepareTea)
t.start()
 
