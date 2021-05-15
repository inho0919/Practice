year = input()
ant = year.split()
year1 = int(ant[0])
year2 = int(ant[1])

temp = "no"

if year2 == 1 or year2 == 3 or year2 == 5 or year2 == 7 or year2 == 8 or year2 == 10 or year2 == 12:
    print("31")
elif year2 == 2:
    if year1%4 == 0 and year1%100 != 0:
        temp = "yes"

    if year1%400 == 0:
        temp = "yes"
    
    if temp == "yes":
        print("29")
    else:
        print("28")
else:
    print("30")
