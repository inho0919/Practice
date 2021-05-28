num = input()
a = list()
a = num.split(' ')
n = int(a[0])
r = int(a[1])

ncount = 1
rcount = 1
ccount = 1

for i in range(1, n+1):
  ncount = ncount * i

for i in range(1, r+1):
  rcount = rcount * i

for i in range(1, n-r+1):
  ccount = ccount * i

total = rcount * ccount

same = ncount / total

print(int(same))
