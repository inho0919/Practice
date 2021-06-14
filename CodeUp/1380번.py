line = int(input())

a = 1
b = 1

for i in range(a, 7):
  for j in range(6, b-1, -1):
    if(line == i + j):
      print(str(i), end=" ")
      print(str(j))
