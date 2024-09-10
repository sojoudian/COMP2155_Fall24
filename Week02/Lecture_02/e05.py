filename = input("Enter a file name: ")
file = open(filename, 'r')
content = file.read()
print(content)

file.close()