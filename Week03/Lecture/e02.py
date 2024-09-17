class Dog:
    def __init__(self, name, breed):
        self.name = name # Attribute
        self.breed = breed # Attribute

    def bark(self):
        return f"{self.name} barked!"

my_dog = Dog("Fendi", breed="Golden Retriever")

print(my_dog.bark())