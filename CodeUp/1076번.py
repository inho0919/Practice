a = input()
txt = ord(a)
temp = 97

alpha = txt - temp

for i in range(0, alpha+1):
    print(chr(temp + i), end=' ')
