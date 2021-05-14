item = input()
line = list(item)

new = line[1] + line[0]

sys = int(new) * 2

if((sys%100)<=50):
    print(sys%100)
    print("GOOD")
else:
    print(sys%100)
    print("OH MY GOD")
