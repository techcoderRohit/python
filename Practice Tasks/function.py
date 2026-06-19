#1. write a function to calculate and return the square of a number

def square(num):
    return num ** 2

result = square(4)
print(result)

#2. create a function that takes two parameters and returns their sums

def add(num1,num2):
    return num1 + num2

print(add(5,10))

#3. write a function multiply that multiplies two nummbers, but can also accept and multiply strings

def multiply(p1, p2):
    return p1*p2

print(multiply(5, 6))
print(multiply('a', 6))
print(multiply(5, 'b'))

#4. create a function that returns both the area and circumference of a circle given its radius
import math
def circle(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle(4)

print("Area:", a)
print("Circumference: ", c)
