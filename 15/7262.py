# ((x & 32765 != 0) or (x & 22635 != 0)) <= (x & a > 0)

for a in range(1, 100000):
    if all( (((x & 32765 != 0) or (x & 22635 != 0)) <= (x & a > 0)) for x in range(0, 100000)) is True:
        print(a)
        break
