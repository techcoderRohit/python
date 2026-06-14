#if statement
age = 20
if age >= 18:
    print("Eligible for vote")

#short- hand if
age = 21 
if age > 18 : print("Eligible for vote")

#if - else statement
age = 10
if age <= 12:
    print("Travel for free")
else:
    print("pay for ticket")

#if - elif statement
age = 25
if age <= 12:
    print('Child')
elif age <= 19:
    print('Teenager')
elif age <= 35:
    print('Young Adult')
else:
    print('Adult')

#nested if statement

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% Senior discount")
    else:
        print("20% Senior discount")
else:
    print("Not eligible for a senior discount")

#conditional expression

age = 20
s = 'adult' if age >= 18 else 'minor'
print(s)

#match case statement

number = 2
match number:
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
    case _:
        print('other number')

