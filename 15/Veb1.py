# (x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(((x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))) for x in range(1, 1000)) is True:
        print(a)
        break
