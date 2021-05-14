num = input()
new = num.split(" ")

year = list(new[0])
years = int(year[0]+year[1])

now = 2013

if(new[1] == "1" or new[1] == "2"):
    ages = 1900 + years
    age = now - ages
else:
    ages = 2000 + years
    age = now - ages

print(age)
