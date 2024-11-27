## Thread Subclass Examplepython

from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print(f"Count: {i}")

thread = MyThread()
thread.start()
thread.join()

