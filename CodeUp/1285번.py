a = input()
nu = list()
s = ""
p = list()

for i in range(0, len(a)-1):
    if a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/":
        nu.append(a[i])

for i in range(0, len(a)):
    if a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/" or a[i] == "=":
        p.append(s)
        s = ""
    else:
        s = s + a[i]

total = int(p[0])
for i in range(1, len(nu)):
    if nu[i-1] == "+":
        total = int(total + int(p[i]))
    elif nu[i-1] == "-":
        total = int(total - int(p[i]))
    elif nu[i-1] == "*":
        total = int(total * int(p[i]))
    elif nu[i-1] == "/":
        total = int(total / int(p[i]))

if nu[len(nu) - 1] == "+":
    print(int(total + int(p[len(p)-1])))
elif nu[len(nu) - 1] == "-":
    print(int(total - int(p[len(p)-1])))
elif nu[len(nu) - 1] == "*":
    print(int(total * int(p[len(p)-1])))
elif nu[len(nu) - 1] == "/":
    print(int(total / int(p[len(p)-1])))
