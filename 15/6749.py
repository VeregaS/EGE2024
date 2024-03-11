# (x + 2 * y > a) or (y < x) or (x < 30)

for a in range(10**3, 0, -1):
    if all( ((x + 2 * y > a) or (y < x) or (x < 30)) for x in range(10**3) for y in range(10**3) ):
        print(a)
        break
