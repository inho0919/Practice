num1 = input()
num2 = input()
num3 = input()

a = num1.split(' ')
b = num2.split(' ')
c = num3.split(' ')

a1 = int(a[0]) * int(a[1])
b1 = int(b[0]) * int(b[1])
c1 = int(c[0]) * int(c[1])

if (a1 > b1):
  if(a1 > c1):
    print(a1)
  else:
    print(c1)
elif (b1 > a1):
  if(b1> c1):
    print(b1)
  else:
    print(c1)
elif (c1>a1):
  if(c1> b1):
    print(c1)
  else:
    print(b1)
