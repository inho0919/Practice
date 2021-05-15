year = input()
ant = year.split()
year1 = int(ant[0])
year2 = int(ant[1])
year3 = int(ant[2])

if year2 > (year1 + year3):
    print("advertise")
elif year2 < (year1 + year3):
    print("do not advertise")
else:
    print("does not matter")
