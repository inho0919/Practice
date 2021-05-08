a = input()
b = a.split(" ")

for i in range(0, len(b)):
    if int(b[i]) == 0:
        break
    else :
        print(b[i])
