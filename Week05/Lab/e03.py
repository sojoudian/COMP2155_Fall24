class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the Student class
student1 = Student("John", 20)

# Displaying the student's information
student1.display_info()
