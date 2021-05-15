line = input()

pot = list()

pot = line.split(' ')

a = int(pot[0])
b = int(pot[1])


if(a < b):
  for i in range(a, b+1):
    print(str(i), end=" ")
else:
  for i in range(b, a+1):
    print(str(i), end=" ")
