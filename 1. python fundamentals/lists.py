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

#list comprehension

a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)

a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)

b = [5, 12, 7, 18, 3, 20]
res = [val for val in b if val > 10]
print(res)

#creating a list from a range
a = [i for i in range(10)]
print(a)

#using nested loops
c = [(x, y) for x in range(3) for y in range(3)]
print(c)

#flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)



