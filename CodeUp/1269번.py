alp = input()
pok = list()

pok = alp.split(' ')

a = int(pok[0])
r = int(pok[1])
d = int(pok[2])
n = int(pok[3])


if(n == 1):
  print(a)
else:
  for i in range(2, n+1):
    a = a * r
    a = a + d
  print(a)
