line = input()

pot = list()

pot = line.split(' ')

a = int(pot[0])
b = int(pot[1])

sum = 0

if(a < b):
  for i in range(a, b+1):
    if i %2 == 0:
      sum = sum - i
    else:
      sum = sum + i
else:
  for i in range(b, a+1):
    if i %2 == 0:
      sum = sum - i
    else:
      sum = sum + i

print(sum)
