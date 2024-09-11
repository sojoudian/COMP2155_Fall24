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
        file.write(f"{firstname} {lastname}\n")

# function to read from the file and output the formatted name
def read_student_from_file():
    with open("student_id.txt", "r") as file:
        name = file.read().split()
        firstname = name[0]
        lastname = name[1]
        print(f"The student's first name is {firstname} and the student's last name is {lastname}")



def main():
    # Get user info
    firstname, lastname, student_id = get_user_input()

    # Output summary of user information
    print(summarize_student(firstname, lastname, student_id))

    # Write the first and last name to a file name student_id.txt
    write_student_to_file(firstname, lastname)

    # Read the file and output the formatted name
    read_student_from_file()



if __name__ == "__main__":
    main()


