a = input()
b = a.split(" ")
num1 = int(b[0])
num2 = int(b[1])

for i in range(1, num1+1):
    for j in range(1, num2+1):
        print(str(i) + " " + str(j))
