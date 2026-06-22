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

#decorator example - Timing Function execution

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

#create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
      args_value = ', '.join(str(arg) for arg in args)
      kwargs_value = ', '.join(f"{k} = {v}" for k,v in kwargs.items())
      print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value} ")
      return func(*args, **kwargs)  
    return wrapper

@debug
def greet(name, greeting='hello'):
    print(f"{greeting}, {name}")

greet("chai", greeting="hanji")

#Implement a decorator that caches the return values of a function , so that when it's called with the same arguments , the cached value is returned instead of re-executing the function

def cache_decorator(func):
    cache = {}
    
    def wrapper(n):
        if n in cache:
            print(f"  Returning cached result for {n}")
            return cache[n]
        
        print(f"  Computing result for {n}")
        result = func(n)
        cache[n] = result
        return result
    
    return wrapper

@cache_decorator
def add_numbers(n):
    return n + n + n

# Example: Caching in Action
print("\n--- Simple Caching Example ---")
print(add_numbers(5))   # Computes
print(add_numbers(5))   # Returns cached value
print(add_numbers(10))  # Computes (different argument)
print(add_numbers(5))   # Returns cached value


