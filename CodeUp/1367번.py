num = int(input())

for i in range(1, num+1):
  for j in range(i+1, num+1):
    print(' ', end='')

  for j in range(0,num):
    print('*', end='')
  print()
