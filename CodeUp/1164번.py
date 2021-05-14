num = input()
new = num.split(" ")

num1 = int(new[0])
num2 = int(new[1])
num3 = int(new[2])

temp = "CRASH"

if num1 > 170 and num2 > 170 and num3 > 170:
    temp = "PASS"

print(temp)
