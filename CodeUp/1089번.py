item = input()
oldline = item.split(" ")

line0 = int(oldline[0])
line1 = int(oldline[1])
line2 = int(oldline[2])

temp = line0

for i in range(1, line2):
    temp = temp + line1

print(temp)
