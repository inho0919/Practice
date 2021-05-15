num = input()
son = list()
son = num.split(' ')
a = float(son[0])
b = float(son[1])
temps = (b - a) / 0.01
pot = int(round(temps, 0))

answer = a

for i in range(0, pot+1):
  if(len(str(round(answer, 2))) == 3 or ( str(round(answer, 2))[0] == '-' and len(str(round(answer, 2))) == 4 )):
    tos = str(round(answer, 2)) + '0'
    print(tos, end=' ')
  else:
    print(str(round(answer, 2)), end=' ')
  answer = answer + 0.01
