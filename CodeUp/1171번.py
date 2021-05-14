item = input()
now = item.split(" ")

item2 = int(now[1])
item3 = int(now[2])

if len(str(item2)) == 1:
    klasse = "0" + str(item2)
else:
    klasse = str(item2)

if len(str(item3)) == 1:
    num = "00" + str(item3)
if len(str(item3)) == 2:
    num = "0" + str(item3)
if len(str(item3)) == 3:
    num = str(item3)

total = now[0] + klasse + num

print(total)
