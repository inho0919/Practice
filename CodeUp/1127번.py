mid = input()
fin = input()
itr = input()

mid_line = mid.split(" ")
fin_line = fin.split(" ")
itr_line = itr.split(" ")

total1 = float(mid_line[0]) * float(mid_line[1])
total2 = float(fin_line[0]) * float(fin_line[1])
total3 = float(itr_line[0]) * float(itr_line[1])

alles = total1+total2+total3
print("%.1f"%alles)
