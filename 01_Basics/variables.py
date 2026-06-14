#creating a variable
x = 5
name = "Alex"

print(x)
print(name)

#assigning same value
a = b = c = 10
print(a, b, c)

#assigning different values
x,y,z = 1, 2.5, "python"
print(x, y, z)

#concept of object reference
x = 1
y = x
y = y+1

print(x)
print(y)

#deleting a variable - del keyword is used to delete a variable from memory 

"""x = 15
del x
print(x)"""

#practical Tasks

#1. Swapping two variables

a , b = 5, 10
a, b = b, a
print( a, b)

#2. counting characters in a string

word = "Python"
length = len(word)
print("Length of the word:", length)
