num = input()
list = num.split(" ")
a = int(list[0])
r = int(list[1])
n = int(list[2])

for i in range(0,n-1):
    a = a * r

print(a)
