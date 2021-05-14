num = input()
new = num.split(" ")

num1 = int(new[0])
num2 = int(new[1])

num3 = num1 + num2

temp1 = ""
temp2 = ""
temp3 = ""

if (num1 % 2) == 0:
    temp1 = "짝수"
else :
    temp1 = "홀수"

if (num2 % 2) == 0:
    temp2 = "짝수"
else :
    temp2 = "홀수"

if (num3 % 2) == 0:
    temp3 = "짝수"
else :
    temp3 = "홀수"

print(temp1 + "+" + temp2 + "=" + temp3)
