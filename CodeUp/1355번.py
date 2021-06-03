num = int(input())

for i in range(0, num):
  for j in range(0, i):
    print(' ', end='')
  for j in range(i, num):
    print('*', end='')
  print()
