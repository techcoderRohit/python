username = 'rohit'

def func():
    username = 'chai'
    print(username)

print(username)
func()

x = 99

def func2(y):
    z = x + y
    return z

result = func2(2)
print(result)

x = 10

def func3():
    global x
    x = 12

func3()
print(x)

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()