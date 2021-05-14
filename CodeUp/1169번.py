num = int(input())
real = num - 1
now = 2012

time = now - real

if time < 2000:
    times = int(time%1900)
    print(str(times) + " " + "1")
elif time == 2000:
    print("0 3")
else:
    times = int(time%2000)
    print(str(times) + " " + "3")
