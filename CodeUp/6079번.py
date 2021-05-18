a = int(input())
sum = 0
count = 1

for i in range(0, a):
    if (sum < a):
        sum = sum + i
        count = i

print(count)
