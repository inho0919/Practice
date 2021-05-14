line = input()
a = list()
a = line.split(' ')

a[0]= int(a[0])
a[1]= int(a[1])

try:
  check1 = a[1] / a[0]
except:
  a[0] = 24

temp = (a[0]*60 + a[1] )- 30
hour = int(temp/60)
minute = temp%60

try:
  p = hour - 24
  q = 1 / p
except:
  hour = 0

times = str(hour) + " " + str(minute)
print(times)
