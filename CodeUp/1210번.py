item = input()
new = item.split(" ")

one = int(new[0])
two = int(new[1])

temp1 = 0
temp2 = 0

if one == 1:
    temp1 = 400
elif one == 2:
    temp1 = 340
elif one == 3:
    temp1 = 170
elif one == 4:
    temp1 = 100
else :
    temp1 = 70

if two == 1:
    temp2 = 400
elif two == 2:
    temp2 = 340
elif two == 3:
    temp2 = 170
elif two == 4:
    temp2 = 100
else :
    temp2 = 70

if (temp1+temp2) > 500:
    print("angry")
else:
    print("no angry")
