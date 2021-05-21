c = input()
b = c.split(" ")

a = int(b[0])
m = int(b[1])
d = int(b[2])
n = int(b[3])

for i in range(0, n-1):
    a = a * m
    a = a + d

print(a)
