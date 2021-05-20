a = input()
b = a.split(" ")
num1 = int(b[0])
num2 = int(b[1])
num3 = int(b[2])

count = 0

for i in range(0, num1):
    for j in range(0, num2):
        for k in range(0, num3):
            count = count + 1
            print(str(i) + " " + str(j) + " " + str(k))

print(count)
