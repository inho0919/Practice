a =int(input())

if a<0 and a%2 == 0:
    print("minus")
    print("even")
elif a<0 and a%2 != 0:
    print("minus")
    print("odd")
elif a>0 and a%2 == 0:
    print("plus")
    print("even")
elif a>0 and a%2 != 0:
    print("plus")
    print("odd")
