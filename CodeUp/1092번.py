a = input()
num = a.split(' ')

num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])

count = 1
check = 0

while(check != 1):
    if(count%num[0] == 0 and count%num[1] == 0 and count%num[2] == 0):
        check = 1
    count = count + 1

print(count-1)
