#1. Check if user is eligible to vote

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")

#2. check if a number is positive

num = int(input("Enter num: "))
if num > 0:
    print('The number is positive')

#3. check if a student is pass/fail in exam

marks = int(input("Enter your marks : "))
if marks >= 40:
    print('You passed the exam')
else:
    print('You failed the exam')

#4. check if a user has balance to buy an item

balance = float(input('Enter your balance: '))
price = float(input('Enter the item price: '))

if balance >= price:
    print('purchase successful')
else:
    print('Insufficient funds')

#5. suggest a mode of transport based on distance

distance = float(input("Enter the distance: "))

if distance <= 2:
    print('you can walk')
elif distance <= 10:
    print('use a bicycle or scooter')
elif distance <= 50:
    print('Take a car or public transport')
else:
    print('consider a train or flight')

#6. check the battery status

battery = int(input("Enter battery percentage: "))

if battery > 80:
    print("Battery Full")
elif battery > 40:
    print("Battery Half")
else:
    print("Battery Low")

#7. Login with usename and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Rohit":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Username not found")

#8. check exam pass and scholarship eligibility

marks = int(input("Enter your marks: "))

if marks >= 50:
    if marks >= 80:
        print("Passed with scholarship")
    else:
        print("Passed without scholarship")
else:
    print("Failed")

#9. check if number is even or odd

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

#10. compare two numbers

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("a is greater" if a > b else "b is greater")

#11. Temperature check

temp = int(input("Enter the temperature: "))
print("Hot" if temp > 25 else "Cool")

#12. Activity suggestion based on weather condition

weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

match weather:
    case "sunny":
        print("Great day for a picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Perfect time for a walk.")
    case "snowy":
        print("Build a snowman or go skiing!")
    case _:
        print("Unknown weather condition.")

#13. Mobile notification settings based on user profile mode

mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()

match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")

#14. Assign grades

grade = input("Enter your grade (A/B/C): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Fail")