#creating a Tuple

tup = ()
print(tup)

# Using String
tup = ('Raj', 'Ashu')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Gopi')
print(tup)

tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)

#accessing of tuples

tup = tuple("Ganga river")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Ganga", "river", "is","holy","river")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

#concatenation of tuples

tup1 = (0, 1, 2, 3)
tup2 = ('Rohit','is','a','player')
tup3 = tup1 + tup2
print(tup3)

#slicing of tuple

tup = tuple('BBD UNIVERSITY')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

#deleting a tuple

tup = (0, 1, 2, 3, 4)
del tup
print(tup)
