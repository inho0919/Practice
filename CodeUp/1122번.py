time = int(input())

minute = int(time/60)
second = int(time%60)

minstr = str(minute)
secstr = str(second)

print(minstr + " " + secstr)
