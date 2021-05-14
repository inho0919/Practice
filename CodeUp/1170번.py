a = input()
list = a.split(" ")
if len(list[2]) == 1:
    list[2] = "0" + list[2]

print(list[0]+list[1]+list[2])
