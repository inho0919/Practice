alp = input()
pok = list()

pok = alp.split(' ')

a = str(pok[0])
b = str(pok[1])

a1 = ord(a)
b1 = ord(b)

for i in range(a1, b1+1):
  print(chr(i), end=' ')
