#map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator). It is a higher-order function used for uniform element-wise transformations, enabling concise and efficient code.


#simple example of using map() to convert a list of strings into a list of integers.
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

#converting map object to a list

def double(val):
    return val * 2

a = [1, 2, 3, 4]    
res = list(map(double, a))
print(res)

#map() with lambda

a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a))
print(res)

#map() with multiple iterables

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

#converting strings to uppercase

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

#extracting first character from strings

words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)
print(list(res))

#Removing whitespaces from strings

s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))

#calculate fahrenheit from celsius

celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))




