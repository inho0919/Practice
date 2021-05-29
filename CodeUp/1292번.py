a = input()
sum = 0
for i in range(0, len(a)):
  sum = sum + int(a[i])
b = sum % 7
if(b == 4):
  print('suspect')
else:
  print('citizen')
