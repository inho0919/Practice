num = int(input())

sum = 0

for i in range(1, num+1):
  sum = sum + i

for i in range(1, num+1):
  for j in range(1, i+1):
    print(str(sum), end=' ')
    sum = sum - 1
  print()
