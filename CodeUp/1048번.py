line = input()
a = line.split(" ")

temp = 1
for i in range(0, int(a[1])):
    temp = temp * 2

print(int(a[0]) * temp)
