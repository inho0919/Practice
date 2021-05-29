num = input()

for i in range(0, len(num)):
  temp = ord(num[i])
  if ord(num[i]) <= 90 and ord(num[i]) >=65:
    temp = temp + 32
  elif ord(num[i]) >= 97 and ord(num[i]) <= 122:
    temp = temp - 32
  print(chr(temp), end='')
