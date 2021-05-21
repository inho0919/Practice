c = input()
b = c.split(" ")

a = int(b[0])
d = int(b[1])
n = int(b[2])

for i in range(0, n-1):
    a = a + d

print(a)
