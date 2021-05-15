line = input()
pos = input()
num1 = list()
num2 = list()

num1 = line.split(' ')
num2 = pos.split(' ')

bonus = int(num1[6])

num = 0

for i in range(0, 6):
  for j in range(0, 6):
    if (int(num1[i])== int(num2[j])):
      num = num + 1

count = 0


for i in range(0, 6):
  if int(num2[i])== bonus:
    count = 1


if num <= 2:
  print(0)
elif num == 3:
  print(5)
elif num == 4:
  print(4)
elif num == 5:
  if (count == 0):
    print(3)
  else:
    print(2)
elif num == 6:
  if (count == 1):
    print(2)
  else:
    print(1)
