line = input()

a = int(line)

a_list = list()

for i in range(1, a+1):
  if a % i == 0:
    a_list.append(i)

if(len(a_list) == 2):
  print('prime')
else:
  print('not prime')
