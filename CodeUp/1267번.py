num = int(input())
line = input()
lists = list()

lists = line.split(' ')

sum = 0

for i in range(0, num):
  if int(lists[i])%5 == 0:
    sum = sum + int(lists[i])

print(sum)
