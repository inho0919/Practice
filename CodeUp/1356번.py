num = int(input())

for i in range(0, num):
  if(i == 0 or i == num-1):
    for j in range(0, num):
      print('*', end='')
  else:
    for j in range(0,num):
      if j == 0 or j == num-1:
        print('*', end='')
      else:
        print(' ', end='')
  print()
