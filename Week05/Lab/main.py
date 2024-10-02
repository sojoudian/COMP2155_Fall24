# Importing the Animal class from animal.py
from animal import Animal

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Creating an instance of the Dog class
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks


# In a different file: When the parent class is in a separate file (animal.py), you must import it into the current script (main.py) for the child class to inherit from it.
