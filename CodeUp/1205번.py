item = input()
new = item.split(" ")

one = int(new[0])
two = int(new[1])

temp1 = one + two
temp2 = one * two
temp3 = one
temp4 = two
temp5 = one - two
temp6 = float(one / two)

for i in range(1, two):
    temp3 = temp3 * one

for i in range(1, one):
    temp4 = temp4 * two

if temp1 >= temp2 and temp1 >= temp3 and temp1 >= temp4 and temp1>=temp5 and temp1>=temp6:
    print("%.6f" % temp1)
elif temp2 >= temp1 and temp2 >= temp3 and temp2 >= temp4 and temp2>=temp5 and temp2>=temp6:
    print("%.6f" % temp2)
elif temp3 >= temp1 and temp3 >= temp2 and temp3 >= temp4 and temp3>=temp5 and temp3>=temp6:
    print("%.6f" % temp3)
elif temp4 >= temp1 and temp4 >= temp2 and temp4 >= temp3 and temp4>=temp5 and temp4>=temp6:
    print("%.6f" % temp4)
elif temp5 >= temp1 and temp5 >= temp2 and temp5 >= temp3 and temp5>=temp4 and temp4>=temp6:
    print("%.6f" % temp5)
elif temp6 >= temp1 and temp6 >= temp2 and temp6 >= temp3 and temp6>=temp4 and temp6>=temp5:
    print("%.6f" % temp6)    
