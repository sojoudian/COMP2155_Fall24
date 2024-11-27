
from threading import Thread

def greet(name):
    print(f"Hello, {name}!")

# Get user input for the name
user_name = input("Enter your name: ")

# Create and start the thread
thread = Thread(target=greet, args=(user_name,))
thread.start()
thread.join()