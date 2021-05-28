a = list()
for i in range(0, 5):
  temp = int(input())
  a.append(temp)

for i in range(0, len(a)):
  for j in range(0, i):
    if a[i] > a[j]:
      temp = a[j]
      a[j] = a[i]
      a[i] = temp

print(str(a[0]), end=" ")
print(str(a[len(a)- 1]))
