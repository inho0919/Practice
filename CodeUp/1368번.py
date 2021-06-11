a = input()
b = a.split(" ")

line = int(b[0])
num = int(b[1])
dir = b[2]

if dir == "R": 
    for i in range(0, line):
        for j in range(line, i+1, -1):
            print(" ", end="")
        for j in range(0, num):
            print("*", end="")
        print()
elif dir == "L":
    for i in range(0, line):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0, num):
            print("*", end="")
        print()
