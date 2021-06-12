a = input()
b = a.split(" ")

num1 = int(b[0])
num2 = int(b[1])

for i in range(0, num2):
    for i in range(0, num1):
        for j in range(1, i+1):
            print(" ", end="")
        print("*", end="")
        print()
    for i in range(num1-1, 0, -1):
        for j in range(0, i-1):
            print(" ", end="")
        print("*")
