line = input()
a = line.split(' ')

for i in range(0, len(a)-1):
    maxNum = i;
    for j in range(i+1, len(a)):
        if(a[j] < a[maxNum]):
            maxNum = j

        temp = a[i]
        a[i] = a[maxNum]
        a[maxNum] = temp

print(a)