a=input()
list = a.split(".")

if len(list[0]) == 4:
    list[0] = list[0]
elif len(list[0]) == 3:
    list[0] = "0" + list[0]
elif len(list[0]) == 2:
    list[0] = "00" + list[0]
else:
    list[0] = "000" + list[0]

if len(list[1]) == 1:
    list[1] = "0" + list[1]

if len(list[2]) == 1:
    list[2] = "0" + list[2]
    
print(list[2] + "-" + list[1] + "-" +list[0])
