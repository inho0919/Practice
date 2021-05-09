line = input()
math = line.split(" ")
a = int(math[0])
r = int(math[1])
d = int(math[2])
n = int(math[3])

temp = a

for i in range(1, n):
    temp = temp * r
    temp = temp + d

print(temp)
