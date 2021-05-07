a = input()
num = a.split(" ")
plus = int(num[0]) + int(num[1]) + int(num[2])
temp = len(num)
avg = float(plus/temp)

print(plus)
print("%.1f"%avg)
