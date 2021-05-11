line = input()
a = line.split(' ')

for i in range(0, len(a)-1):
    for j in range(0, (len(a)-1)-i):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)