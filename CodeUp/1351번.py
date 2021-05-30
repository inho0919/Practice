a = input()
b = a.split(' ')
s = int(b[0])
e = int(b[1])

for i in range(s, e+1):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + "=", end='')
        print(str(i*j))
