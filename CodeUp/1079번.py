line = input()
a = line.split(" ")

for i in range(0, len(a)):
    if a[i] == 'q':
        print('q')
        break
    else:
        print(a[i])
