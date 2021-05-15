item = input()
now = item.split(" ")
one = int(now[0])
two = int(now[1])
three = int(now[2])

answer = 0

if(one > 170):
  if(two > 170):
    if(three > 170):
      print('PASS')
    else:
      print('CRASH ' + str(three))
  else:
    print('CRASH ' + str(two))
else:
  print('CRASH ' + str(one))
