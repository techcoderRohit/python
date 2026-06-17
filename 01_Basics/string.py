#creating a string

a = 'Rohit'  
b = "BBD University"  
print(a)
print(b)

#multiline strings

s = """I am Learning
Python String on chai and code"""
print(s)

s = '''I'm a 
Rohit'''
print(s)

#accessing characters in a string

s = "ABCDEF"
print(s[0])   
print(s[4])
print(s[-3])  
print(s[-5])

#string slicing

s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

#looping through strings

s = "ABCDEF"
for char in s:
    print(char)

#string immutability

s = "aBCDEF"
s = "A" + s[1:]  
print(s)

#deleting a string

s = "ABC"
del s

#updating a string

s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)

#common string methods

#len()

s = "chaiandcode"
print(len(s))

#upper() and lower()

s = "Hello World"
print(s.upper())
print(s.lower())

#strip() and replace()

s = "   ABC   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

#concatenation and repetition string

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)

#formatting string

name = "Raj"
age = 22
print(f"Name: {name}, Age: {age}")

s = "My name is {} and I am {} years old.".format( "Rohit", 22)
print(s)

s = "BBD University"
print("BBD" in s)
print("Universe" in s)