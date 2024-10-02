class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

# Creating an instance of the Student class
student1 = Student("John", 20)

# Printing the student object
print(student1)

# Using str() on the student object
print(str(student1))

# • The __str__() method returns a string representation of the object.
# •	When you call print(student1) or str(student1), Python uses the __str__() method to convert the object into a readable string format.
# •	In this example, __str__() returns a formatted string that includes the student’s name and age.
