num = int(input())
count = 1
temp = 0

for i in range(1, num):
    if(temp >= num):
        break
    else:
        temp = temp + count
        count = count + 1
if num == 1:
    print(1)
else:
    print(temp)
