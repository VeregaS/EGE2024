# (x < a) or (y < a) or (y > (x − 5)) or (y < (2 * x − 15))


for a in range(1000):
    if all( ((x < a) or (y < a) or (y > (x - 5)) or (y < (2 * x - 15))) for x in range(1000) for y in range(1000)):
        print(a)
        break