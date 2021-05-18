b = list()
while(True):
    a = input()
    if(a != "0"):
        b.append(a)
    else:
        break

for i in range(0, len(b)):
    print(b[i])
