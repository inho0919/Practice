num = int(input())
line = input()
lists = list()
lists = line.split(' ')

for i in range(0, num):
  for j in range(0, i):
    if(int(lists[i]) > int(lists[j])):
      temp = lists[j]
      lists[j] = lists[i]
      lists[i] = temp

a = int(lists[0])

print(a)
