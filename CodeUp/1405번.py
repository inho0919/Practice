a = int(input())
b = input()
if a == 1:
    print(b)
else:
    c = b.split(" ")
    del c[len(c)-1]
    for i in range(0, len(c)):
        for j in range(i, len(c)):
            print(c[j], end=" ")
        for j in range(0, i):
            print(c[j], end=" ")
        print()
