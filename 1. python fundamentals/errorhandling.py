file = open('hello.txt','w')

try:
    file.write('chai and code')
finally:
    file.close()

with open('hello.txt', 'w') as file:
    file.write('chai aur python')