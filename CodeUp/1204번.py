item = int(input())

if item == 11 or item == 12 or item == 13:
    print(str(item)+"th")
else:
    if item%10 == 1:
        print(str(item)+"st")
    elif item%10 == 2:
        print(str(item)+"nd")
    elif item%10 == 3:    
        print(str(item)+"rd")
    else:
        print(str(item)+"th")
