# (x <= (not(z))) and (not(y) <= x)

print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (x <= (not(z))) and (not(y) <= x) is False:
                print(x, y, z)
