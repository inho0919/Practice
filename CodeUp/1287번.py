num = int(input())

for i in range(2,11):
  for j in range(1, i):
    for k in range(0, num):
      print('*', end='')
  print()
