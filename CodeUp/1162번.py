num = input()
new = num.split(" ")

num1 = int(new[0])
num2 = int(new[1])
num3 = int(new[2])

value = num1 - num2 + num3

if value%10 == 0:
    print("대박")
else:
    print("그럭저럭")
