# Function to get user inputs, first, last name, id
def get_user_input():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    student_id = input("Enter your student id: ")
    #print(firstname, lastname, student_id)
    return firstname, lastname, student_id

# Function to summarize the student information
def summarize_student(firstname, lastname, student_id):
    return f"Student Summary:\nFirst Name: {firstname}\nLast Name: {lastname}\nStudent Id: {student_id}"

# function to write the student's name to a file
def write_student_to_file(firstname, lastname):
    with open("student_id.txt", "w") as file:
        file.write(f"The student's first name is {firstname}\nThe student's last name is {lastname}\n")

# function