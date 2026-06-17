#local variables are defined inside a fuction and exist only during its execution.They cannot be accessed from outside the function.

def myfun():
    msg = "Hello from inside the fubction"
    print(msg)

myfun()

def greet():
    msg = "Hello, Raj!"
    print("Inside function:", msg)

greet()
#print("Outside function:", msg) #NameError : 'msg' is not defined

#Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions.

msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

#use of local variables and global variables

def fun():
    s = "Chai Lover."
    print(s)

s = "I love Coffee"
fun()   
print(s)

#Global vs Local with same name
a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)