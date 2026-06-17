#decorators in python

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()

#higher order functions

def fun(f, x):
    return f(x)

def square(x):
    return x * x
res = fun(square, 5)
print(res)

