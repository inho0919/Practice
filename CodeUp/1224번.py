line = input()

a = list()
a = line.split(' ')

a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
a[3] = int(a[3])

num1 = float(a[0] / a[1])
num2 = float(a[2] / a[3])

if(num1 > num2):
    print('>')
elif(num1 == num2):
    print('=')
else:
    print('<')
