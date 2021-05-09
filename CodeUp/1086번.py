num = input()
new = num.split(" ")

total = int(new[0]) * int(new[1]) * int(new[2]) * int(new[3])

mega = float(((total/8) / 1024)/ 1024)
print(("%.1f" % mega) +" MB")
