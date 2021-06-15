a = int(input())
b = input()

c = b.split(" ")

for i in range(0, len(c)):
    for j in range(0, len(c)):
        if i > j:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp

for i in range(0, len(c)):
    print(c[i], end=" ")
