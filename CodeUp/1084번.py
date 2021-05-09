num = input()
new = num.split(" ")

count = 0

for i in range(0, int(new[0])):
    for j in range(0, int(new[1])):
        for k in range(0, int(new[2])):
            print(str(i) + " " + str(j) + " " + str(k))
            count = count + 1

print(count)
