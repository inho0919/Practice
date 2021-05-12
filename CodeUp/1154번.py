item = input()
oldline = item.split(" ")

num1 = int(oldline[0])
num2 = int(oldline[1])

if num1>num2 :
    print(num1-num2)
else:
    print(num2-num1)
