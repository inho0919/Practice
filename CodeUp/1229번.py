item = input()
lep = list()

lep = item.split(' ')

h = float(lep[0])
w = float(lep[1])

std = 0

if h < 150:
  std = h - 100
elif h >= 160:
  std = (h - 100) * 0.9
else:
  std = (h - 150) / 2 + 50

total = (w - std) * 100 / std

if float(total) > 20 :
  print('비만')
elif float(total)<=10:
  print('정상')
else:
  print('과체중')
