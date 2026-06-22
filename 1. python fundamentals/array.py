#numpy array
import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
res = np.array([[1, 2], [3, 4]])
print(res * 2)

#create an array
import array as arr
a = arr.array('i', [1, 2, 3])

# accessing first array
print(a[0])

# adding element to array
a.append(5)
print(a)

#adding elements

import array as arr
a = arr.array('i', [1, 2, 3])
print(*a)

a.insert(1, 4)  # Insert 4 at index 1
print(*a)

#accessing elements

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])

print(a[0])
print(a[3])

b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])

#removing elements

import array
a = array.array('i', [1, 2, 3, 1, 5])

# remove first occurence of 1
a.remove(1)
print(a)

# remove item at index 2
a.pop(2)
print(a)

#array slicing

import array as arr
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)

res = b[3:8]
print(res)

res = b[5:]
print(res)

res = b[:]
print(res)

#searching elements

import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# index of 1st occurrence of 2
print(a.index(2))

# index of 1st occurrence of 1
print(a.index(1))

#updating elements

import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# update item at index 2
a[2] = 6
print(a)

# update item at index 4
a[4] = 8
print(a)

#operations on array

#counting elements

import array
a = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = a.count(2)
print(count)

#reversing elements

import array
a = array.array('i', [1, 2, 3, 4, 5])
a.reverse()
print(*a)

#extend element

import array as arr 
a = arr.array('i', [1, 2, 3,4,5])
a.extend([6,7,8,9,10])
print(a)
