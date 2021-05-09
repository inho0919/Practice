num = int(input())
temp = 1
d = 2
count = 1

for i in range(1, num):
    if temp < num:
        temp = temp + d
        d = d + 1
        count = i
    else:
        break
print(count+1)
