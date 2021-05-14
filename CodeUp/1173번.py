item = input()
now = item.split(" ")

hour = int(now[0])
minute = int(now[1])

if (minute-30) < 0 :
    if hour == 0:
        hour = 24
    hour = hour - 1
    res = minute - 30
    minute = 60 + res
else:
    minute = minute - 30

print(str(hour) + " " + str(minute))
