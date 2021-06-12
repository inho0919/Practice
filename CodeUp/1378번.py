num = int(input())

count = 1
sum = 0

a = list()

for i in range(0, num):
  sum = sum + count
  count = count + 1
  a.append(sum)

sums = 0
for i in range(0, num):
  sums = sums + a[i]

print(sums)
