# keyword is used to refer to a current instance (object) of a class
class MyClass:
    def __init__(self, name):
        self.name = name  # 'self' refers to the current instance

    def greet(self):
        return f"Hello, {self.name}!"

# Creating an instance of MyClass
obj = MyClass("Alice")
print(obj.greet())  # Output: "Hello, Alice!"

# In the example, self refers to the instance obj when methods are called on it.
# In other programming languages, the equivalent keyword may vary:
#
#	•	this in Java, C++, JavaScript, etc.
#	•	self in Python, Ruby, etc.
