num = int(input(), 16)
hexa = "%X" % num
hexa1 = str(hexa)

for i in range(1, 16):
    hexa2 = "%X" % i
    mux = i * num
    print(hexa1 + "*" + str(hexa2) + "=" + str("%X" % mux))
