alp = input()
pok = list()

pok = alp.split(' ')

k = int(pok[0])
h = int(pok[1])

if(h%2 == 0):
  h = (h/2) * 10
else:
  h = (h+1)/2


if(k%2 == 0):
  k = (k/2) * 10
else:
  k = (k+1)/2


print(int(k + h))
