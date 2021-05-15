line = input()

a = list()

a = line.split(' ')

a[0] = float(a[0])
a[1] = float(a[1])

std = (a[0] - 100.0) * 0.9

bim = ((a[1] - std) * 100.0) / std

bim = '%.2f' % bim

if float(bim) > float(20):
  print('비만')
elif float(bim) <= float(10):
  print('정상')
else:
  print('과체중')
