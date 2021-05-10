line = input()
a = line.split("C")
txt = a[1]

chem = txt.split("H")

c = int(chem[0])
h = int(chem[1])

print((c*12) + (h*1))
