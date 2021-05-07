num = input()
line = num.split(" ")

print(int(line[0]) + int(line[1]))
print(int(line[0]) - int(line[1]))
print(int(line[0]) * int(line[1]))

so = int(line[0]) / int(line[1])

print(int(so))
print(int(line[0]) % int(line[1]))

div = float(int(line[0])/int(line[1]))

print("%.2f"%div)
