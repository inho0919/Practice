item = input()
now = item.split(" ")


for i in range(0, 3):
    for j in range(0, 3):
        if int(now[i]) <= int(now[j]):
            temp = int(now[i])
            now[i] = int(now[j])
            now[j] = temp

print(str(now[0]) + " " + str(now[1]) + " " + str(now[2]))
