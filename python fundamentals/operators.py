#arithmetic operators

a = 16
b = 12

print("Addition: ", a + b)
print("Substraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Floor Division: ", a // b)
print("Modulus: ", a % b)
print("Exponentiation: ", a ** b)

#comparison operators

a = 13
b= 33

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

#logical operators - and, or , not

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)

#Bitwise operators - &, |, ~, ^, >>, <<

a = 10
b = 4

print(a & b)
print(a | b)
print(a >> b)
print(a << b)
print(~a)
print(a ^ b)

#assignment operators

a = 10 
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#identity operators - is , is not

a = 10
b = 20
c = a
print(a is not b)
print(a is c)

#ternary operator 

a, b = 10, 20
min = a if a < b else b
print(min)

#operator precendence

expr = 10 + 20 * 30
print(expr)

print(100 / 10 * 10)
print(5 - 2 + 3)
print(4 - (6 + 7))
print(2 ** 3 ** 2)
