line = input()
a = line.split(" ")
a1 = int(a[0])
a2 = int(a[1])
mul = a1%a2
plus = a1+a2
minus = a1-a2
ex = a1*a2
div = int(a1/a2)

print(a[0] + " + " + a[1] + " = " + str(plus))
print(a[0] + " - " + a[1] + " = " + str(minus))
print(a[0] + " * " + a[1] + " = " + str(ex))
print(a[0] + " / " + a[1] + " = " + str(div))
print(a[0] + " % " + a[1] + " = " + str(mul))
