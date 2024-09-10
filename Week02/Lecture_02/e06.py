filename = input("Enter a file name: ")
file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    print(line, end='')