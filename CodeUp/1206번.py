item = input()
new = item.split(" ")

one = int(new[0])
two = int(new[1])

div = 0
if one >=two:
    if one%two == 0:
        div = int(one/two)
        print(str(two)+"*"+ str(div) +"="+str(one))
    else:
        print("none")
else:
    if two%one == 0:
        div = int(two/one)
        print(str(one)+"*"+ str(div) +"="+str(two))
    else:
        print("none")
