#creating deque
from collections import deque 
d = deque(['name','age','DOB']) 
print(d)

#accessing items in deque
from collections import deque
dq = deque([1, 2, 3, 4])

print(dq[0])
print(dq[-1])

#operations on deque

#append() - adds an element to the right end of the deque.
from collections import deque
dq = deque([10, 20, 30])
dq.append(40)
print(dq)

#appendleft(): adds an element to the left end of the deque.
from collections import deque
dq = deque([10, 20, 30])
dq.appendleft(5)
print(dq)

#extend(): adds multiple elements to the right end of the deque.
from collections import deque
dq = deque([10, 20, 30])
dq.extend([40, 50, 60])
print(dq)

#extendleft(): adds multiple elements to the left end of the deque.
from collections import deque
dq = deque([10, 20, 30])
dq.extendleft([1, 2])
print(dq)

#remove(): removes the first occurrence of a specified value.
from collections import deque
dq = deque([10, 20, 30, 20])
dq.remove(20)
print(dq)

#pop(): removes and returns the element from the right end.
from collections import deque
dq = deque([10, 20, 30])
dq.pop()
print(dq)

#popleft(): removes and returns the element from the left end.
from collections import deque
dq = deque([10, 20, 30])
dq.popleft()
print(dq)

#clear(): removes all elements from the deque.
from collections import deque
dq = deque([10, 20, 30])
dq.clear()
print(dq)

#len(): returns the total number of elements in the deque.
from collections import deque
dq = deque([1, 2, 3, 4, 5])
print(len(dq))

#rotate(): rotates the elements of the deque.
from collections import deque
dq = deque([10, 20, 30, 40])
dq.rotate(1)
print(dq)

#reverse(): reverses the order of elements in the deque.
from collections import deque
dq = deque([10, 20, 30, 40])
dq.reverse()
print(dq)

#count(): returns how many times a specific element appears in the deque.
from collections import deque
dq = deque([10, 20, 30, 20, 40, 20])
print(dq.count(20))



