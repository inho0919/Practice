item = input()
oldline = item.split(" ")

num1 = int(oldline[0])
num2 = int(oldline[1])
num3 = int(oldline[2])

if num1 >= num2 and num1 >= num3:
    if num2+num3 > num1:
        print("yes")
    else:
        print("no")
elif num2 >= num1 and num2 >= num3:
    if num1+num3 > num2:
        print("yes")
    else:
        print("no")
elif num3 >= num1 and num3 >= num2:
    if num2+num1 > num3:
        print("yes")
    else:
        print("no")
