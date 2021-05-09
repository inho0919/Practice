num = input()
new = num.split(" ")

num1 = int(new[0])
num2 = int(new[1])
for i in range(1, num1+1):
    for j in range(1, num2+1):
        print(i, end=" ")
        print(j)
