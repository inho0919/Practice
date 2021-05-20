a = input()
b = a.split(" ")
num1 = int(b[0])
num2 = int(b[1])
num3 = int(b[2])
num4 = int(b[3])

total = num1 * num2 * num3 * num4

total = total / 8
total = total / 1024
total = total / 1024

print("%.1f" % total, end=" MB")
