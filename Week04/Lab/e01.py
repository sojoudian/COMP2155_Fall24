class Student:
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    def get_s_id(self):
        return self.studentID

s = Student("Maz", 36, 100223344)
# Access the attribute:
print(s.name)

# Access the method of the class
print(s.get_s_id())

