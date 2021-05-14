item = input()
now = item.split(" ")
one = int(now[0])
two = int(now[1])
time = 90
temp = 0

while(one < time):
    one = one + 5
    temp = temp + 1

print(temp+two)
