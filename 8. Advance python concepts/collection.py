#creating a counter
from collections import Counter
# Create a list of items
a = [1, 1, 1, 2, 3, 3, 4]

# Use Counter to count occurrences
cnt = Counter(a)
print(cnt)

from collections import Counter
ctr1 = Counter([1, 2, 2, 3, 3, 3]) # From a list
ctr2 = Counter({1: 2, 2: 3, 3: 1}) # From a dictionary
ctr3 = Counter('hello') # From a string

print(ctr1)
print(ctr2)
print(ctr3)

#accessing counter elements
from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])

# Accessing count of an element
print(ctr[1])  
print(ctr[2])  
print(ctr[3])  
print(ctr[4])  # (element not present)

#counter methods

#update()
from collections import Counter
ctr = Counter([1, 1, 2])
ctr.update([2, 2, 3, 3])
print(ctr)

#elements()
from collections import Counter
ctr = Counter([1, 1, 2, 2, 2, 3])
items = list(ctr.elements())
print(items)

#most_common()
from collections import Counter
ctr = Counter([1, 2, 2, 2, 3, 3, 3, 3])
common = ctr.most_common(2)
print(common)

#increasing count manually
from collections import Counter
ctr = Counter([1, 1, 2, 3])

ctr[2] += 2
ctr[4] += 1
print(ctr)

#substract
from collections import Counter
ctr = Counter([1, 1, 2, 2, 2, 3])
ctr.subtract([2, 2, 3])
print(ctr)

#arithmetic operations on counter
from collections import Counter
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union

