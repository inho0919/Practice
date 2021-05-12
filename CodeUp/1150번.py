item = input()
oldline = item.split(" ")

num1 = int(oldline[0])
num2 = int(oldline[1])
num3 = int(oldline[2])

if num1 >= num2 :
    if num2>=num3:
        print(num3)
    else:
        print(num2)
elif num2 >= num3:
    if num3>= num1 :
        print(num1)
    else :
        print(num3)
elif num3>= num1:
    if num1 >= num2:
        print(num2)
    else:
        print(num1)
