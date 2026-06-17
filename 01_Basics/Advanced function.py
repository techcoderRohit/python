#recursion in python

def factorial(n):
    if n == 0:     #Base case
        return 1
    else:          #recursive case
        return n * factorial(n-1) 
    
print(factorial(5))

#pint fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

#lambda fuction

a = 'Pusphendra Singh'
upper = lambda x: x.upper()  
print(upper(a))

#condition check using lambda function
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))

#list comprehension

fun = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in fun:
    print(i())

#returning multiple results

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

#filter

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

#map

a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))

#reduce

from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)