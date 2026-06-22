#opening a file
f = open("rohit.txt", "r")
print(f)

#closing a file
file = open("rohit.txt", "r")
# Perform file operations
file.close()

#checking file operations
f = open("rohit.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

#reading a file
file = open("rohit.txt", "r")
content = file.read()
print(content)
file.close()

#writing a file
with open("rohit.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

with open("rohit.txt", "r") as file:
    content = file.read()
    print(content)

#handling exceptions when closing a file
try:
    file = open("rohit.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()

#file mode

#read mode('r')
with open('example.txt', 'r') as file:
    content = file.read()

#write mode('w')
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

#append mode('a')
with open('example.txt', 'a') as file:
    file.write('\nThis is a new line.')

#binary mode('b')
with open('image.png', 'rb') as file:
    data = file.read()
    # Process the binary data

#read and write mode('r+')
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('\nThis is a new line.')

#write and read mode('w+')
with open('example.txt', 'w+') as file:
    file.write('Hello, world!')
    file.seek(0)
    content = file.read()


