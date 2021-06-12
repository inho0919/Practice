a = int(input())

for i in range(0, a):
    for j in range(a, i+1, -1):
        print(" ", end="")
    for j in range(0, 1):
        print("*",end = "")
    for j in range(i, 0, -1):
        print(" ", end="")
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, 1):
        print("*",end = "")
    print()
for i in range(0, a):
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, 1):
        print("*",end = "")
    for j in range(a, i+1, -1):
        print(" ", end="")
    for j in range(a, i+1, -1):
        print(" ", end="")
    for j in range(0, 1):
        print("*",end = "")
    print()
