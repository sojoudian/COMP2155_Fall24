# Parent class defined in the same script
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Creating an instance of the Dog class
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks

# •	In the same script: The parent class Animal is in the scope of the script, so the child class Dog can directly inherit from it.
