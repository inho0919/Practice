year = int(input())
temp = "no"

if year%4 == 0 and year%100 != 0:
    temp = "yes"

if year%400 == 0:
    temp = "yes"

print(temp)
