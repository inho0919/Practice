line = input()
num = line.split(' ')

num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])

count = 1
check = False

while(check == False):
    if(count%num[0] == 0 and count%num[1] == 0 and count%num[2] == 0): 
        check = True
    count = count + 1

print(count - 1)
