## Basic Thread Without Arguments

from threading import Thread

def display():
    print("Hello from thread!")

thread = Thread(target=display)
thread.start()
thread.join()

