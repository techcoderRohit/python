#creating a set

s = {1, 2, 3, 4}
print(s)

s = set()
print(s)

s = set("Chaiandcode")
print(s)

# Creating a Set with the use of a List
s = set(["chai", "and", "code"])
print(s)

# Creating a Set with the use of a tuple
t = ("chai", "milk", "tea")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"chai": 1, "and": 2, "code": 3}
print(set(d))

#adding element

s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(s)

#accessing a set

s = { 1,2,3,4,5}

for i in s:
    print(i, end=" ")

print("\n", 2 in s)

#removing elements from the set

s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)  

s.discard(4)
print(s)  

s.discard(10)  
print(s)

s = {1, 2, 3, 4, 5}
val = s.pop()
print(val)
print(s)

s = {1, 2, 3, 4, 5}
s.clear()
print(s)

#frozen set

fs = frozenset([1, 2, 3, 4, 5])
print(fs)  

s = {3, 1, 4, 1, 5}
fs = frozenset(s)
print(fs)


