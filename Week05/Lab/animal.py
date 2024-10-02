# Example 2: Parent class imported from another module
# Suppose the parent class is defined in a file named animal.py.


# animal.py
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


# In a different file: When the parent class is in a separate file (animal.py), you must import it into the current script (main.py) for the child class to inherit from it.    
