a = input()
b = a.split(" ")

c = int(b[0])
d = int(b[1])
e = int(b[2])

sum = c + d + e
avg = float(sum / 3)

print(str(sum), end = " ")
print("%.2f" % avg)
