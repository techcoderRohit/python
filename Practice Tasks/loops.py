#1. Print each item in a shopping list

items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy:", item.strip())

#2. Print squares of numbers from 1 to n

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("Square of", i,"is", i**2)

#3. countdown timer

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print("Time left:", seconds)
    seconds -= 1

#4. Sum until user enters 0

total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total sum:", total)

#5. Print multiplication table

n = 3

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

#6. Print identify matrix pattern

n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()  # move to the next row

#7. Stop printing at a target item

items = ["apple", "banana", "cherry", "stop", "mango"]

for item in items:
    if item == "stop":
        break
    print("Item:", item)

#8. find first even number

while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("First even number found:", num)
        break

#9. skip out-of-stock items

items = ["milk", "bread", "out of stock", "eggs"]

for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)

#10. skip even numbers 

n = 10

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print("Odd number:", i)


#11. reverse a string using loops

str = "python"
rev_str = ""

for char in str:
    rev_str = char + rev_str

print(rev_str)

#!2. find the first non - repeated characters

str = "teeter"

for char in str:
    if str.count(char) == 1:
        print("Char is: ",char)
        break

#13. factorial number using while loop

number = 5
fact = 1

while number > 0:
    fact = fact * number
    number = number - 1

print("Factorial:", fact)

#14. check if number is a prime

number = 29
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)

#15. List uniqueness checker

items = ["apple","banana","orange","mango","apple"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)




    
