a = int(input())

row = int((a + 1) /2)


for i in range(0, row):
    for j in range(i, row-1): 
        print(" ",end="")
    for j in range(0, (i+1)*2-1):
        print("*", end="")
    print()
