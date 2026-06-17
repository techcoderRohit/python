#creating a function

def fun():
    print("Welcome to python world")

#calling a function

def fun():
    print("Hello Rohit")
    
fun()

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#Types of function arguments

#default argument

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#keyword argument

def student(fname, lname):
    print(fname, lname)

student(fname='siya', lname='sharma')
student(lname='sharma', fname='siya')

#positional arguments

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("raj", 27)

print("Case-2:")
nameAge(27, "raj")

#Arbitrary arguments

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='raj', mid='for', last='gautam')

# *args example
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'India')

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')

#using both *args and **kwargs

def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Dora", Age=20, City="Japan")

#function within functions

def f1():
    s = 'I love India'
    def f2():
        print(s)
        
    f2()
f1()

#return statement

def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))

#pass by reference and pass by value

def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)

