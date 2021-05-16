line = int(input())

for i in range(1, 10):
  a = str(line) + '*' + str(i) + "=" + str(i*line)
  print(a)
