#for loop

n = 4
for i in range(0, n):
    print(i)

a = ['python','c','java']
for idx in range(len(a)):
    print(a[idx])

#while loop 

count = 0
while (count < 3):
    count = count + 1
    print('Hello world')

#nested loops

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()