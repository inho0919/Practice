a = input()
list = a.split(" ")
com1 = int(list[0])
com2 = int(list[1])
com3 = int(list[2])

if com1%2 == 0:
    com1 = str(com1)
    com1 = "even"
else:
    com1 = str(com1)
    com1 = "odd"
    
if com2%2 == 0:
    com2 = str(com2)
    com2 = "even"
else:
    com2 = str(com2)
    com2 = "odd"
    
if com3%2 == 0:
    com3 = str(com3)
    com3 = "even"
else:
    com3 = str(com3)
    com3 = "odd"
    
print(com1)
print(com2)
print(com3)
