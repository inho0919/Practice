num = int(input())
line = input()
lists = list()

lists = line.split(' ')

sum = 0

for i in range(0, num):
  sum = sum + int(lists[i])

print(sum)
