item = input()
oldline = item.split(" ")

num1 = float(oldline[0])
num2 = float(oldline[1])
num3 = float(oldline[2])

avg = float((num1+num2+num3)/3)
print("%.2f"%avg)
