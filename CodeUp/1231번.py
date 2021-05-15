item = input()

now1 = list()
now2 = list()
now3 = list()
now4 = list()

try:
  now1 = item.split("+")
  if(len(now1) != 1):
    total = int(now1[0]) + int(now1[1])
    print(int(total))
except:
  pass

try:
  now2 = item.split("-")
  if(len(now2) != 1):
    total = int(now2[0]) - int(now2[1])
    print(int(total))
except:
  pass

try:
  now3 = item.split("*")
  if(len(now3) != 1):
    total = int(now3[0]) * int(now3[1])
    print(int(total))
except:
  pass

try:
  now4 = item.split("/")
  if(len(now4) != 1):
    total = int(now4[0]) / int(now4[1])
    print(round(total,2))
except:
  pass
