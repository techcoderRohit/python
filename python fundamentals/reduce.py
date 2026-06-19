#reduce() function (from the functools module) applies a function cumulatively to the elements of an iterable and returns a single final value.

from functools import reduce
a = ["Rohit", "Puneet", "Ratan"]
r = reduce(lambda x, y: x + " " + y, a)
print(r)

#add all numers in a list using reduce()

from functools import reduce
a = [2, 4, 6, 8]
r = reduce(lambda x, y: x + y, a)
print(r)

#using reduce() with lambda function

from functools import reduce
a = [5, 9, 3, 12, 7]
r = reduce(lambda x, y: x if x > y else y, a)
print(r)