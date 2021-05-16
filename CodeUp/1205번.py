item = input()
new = item.split(" ")

one = int(new[0])
two = int(new[1])

temp1 = float(one + two)
temp2 = float(two + one)
temp3 = float(one - two)
temp4 = float(two - one)
temp5 = float(one * two)
temp6 = float(two * one)
temp7 = float(one / two)
temp8 = float(two / one)
temp9 = float(one ** two)
temp10 = float(two ** one)

a = list()
a.append(temp1)
a.append(temp2)
a.append(temp3)
a.append(temp4)
a.append(temp5)
a.append(temp6)
a.append(temp7)
a.append(temp8)
a.append(temp9)
a.append(temp10)

for i in range(0, len(a)):
    for j in range(0, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("%.6f" % a[0])
