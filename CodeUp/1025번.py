a = int(input())
a1 = a/10000
a2 = (a%10000)/1000
a3 = (a%1000)/100
a4 = (a%100)/10
a5 = (a%10)

b1 = int(a1)
b2 = int(a2)
b3 = int(a3)
b4 = int(a4)
b5 = int(a5)

print("[" + str(b1*10000) + "]")
print("[" + str(b2*1000) + "]")
print("[" + str(b3*100) + "]")
print("[" + str(b4*10) + "]")
print("[" + str(b5) + "]")
