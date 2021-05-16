line = input()
co = list()

co = line.split(' ')

count = 0
for i in range(0, len(co)):
  if(int(co[i]) % 5 == 0):
    print(int(co[i]))
    count = count + 1
    break

if(count == 0):
  print(0)
