#creating a list

a = [1, 2, 3]
print(a)

b = ["apple", "banana"]
print(b)

#using list() constructor

a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("mango")
print(b)

#creating list with repeated elements

a = [2] * 5
b = [0] * 7

print(a)
print(b)

a = [1, 2, 2, "Python"]
print(a[0])   # index-based
print(a)

#accessing elements

a = [10, 20, 30]
print(a[0])
print(a[-1])

#adding elements - append, insert, and extend

a = [1, 2]
a.append(3)
print(a)

a = [1, 3]
a.insert(1, 2)
print(a)

a = [1, 2]
a.extend([3, 4])
print(a)

#updating elements

a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

#removing elements - remove, pop, del, clear

a = [1, 2, 3]
a.remove(2)
print(a)

a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3]
a.clear()
print(a)

#iterate over lists

a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

#nested lists

a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])



