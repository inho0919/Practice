item = input()
new = item.split(" ")
count = 0

for i in range(0, 4):
    if(new[i] == "1"):
        count = count + 1

if count == 1 :
    print("도")
elif count == 2 : 
    print("개")
elif count == 3 : 
    print("걸")
elif count == 4 : 
    print("윷")
else:
    print("모")
