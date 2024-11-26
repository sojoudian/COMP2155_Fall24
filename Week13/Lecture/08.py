from threading import Thread
from time import sleep

# Define Theatre class
class Theatre:
    def __init__(self, str):
        self.str = str

    def movieshow(self):
        for i in range(1, 6):
            print(self.str, ":", i)
            sleep(1)

# Create two instances of the Theatre class
obj1 = Theatre("Cut Ticket")
obj2 = Theatre("Show Chair")

# Create threads for the objects
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

# Start the threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

