a = input()
b = a.split(" ")

num1 = int(b[0])
num2 = int(b[1])
num3 = int(b[2])

if num1 < num2:
    if num1 < num3:
        print(num1)
    else:
        print(num3)
elif num1 > num2:
    if num2 > num3:
        print(num3)
    else:
        print(num2)
elif num1 == num2:
    if num1 > num3:
        print(num3)
    else:
        print(num1)
