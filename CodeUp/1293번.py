num = int(input())
line = input()
arr = line.split(' ')

narr = list()

for i in range(0, len(arr)):
  if(arr[i] != ''):
    narr.append(arr[i])

for i in range(0, len(narr)):
  narr[i] = int(narr[i])


    
for i in range(0, len(narr)):
  for j in range(0, i):
    if narr[i] > narr[j]:
      temp = narr[i]
      narr[i] = narr[j]
      narr[j] = temp

print(narr[0], end=' ')
print(narr[len(narr)-1], end=' ')
