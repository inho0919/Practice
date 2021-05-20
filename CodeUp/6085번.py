a = input()
b = a.split(" ")
num1 = int(b[0])
num2 = int(b[1])
num3 = int(b[2])

total = num1 * num2 * num3
total = total / 8
total = total / 1024
total = total / 1024

print("%.2f" % total, end=" MB")
