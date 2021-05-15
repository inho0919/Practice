item = input()
now = item.split(" ")
one = int(now[0])
two = int(now[1])
three = int(now[2])

time = 90
temp = 0

while(one < time):
    one = one + 5
    temp = temp + 1

total = temp + two

if total < three:
  print('lose')
elif total > three:
  print('win')
else:
  print("same")
