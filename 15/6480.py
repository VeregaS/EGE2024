p = [i for i in range(10, 22)]
q = [i for i in range(13, 39)]
r = [i for i in range(18, 26)]

a = []

# (not((x in q) <= ((x in p) or (x in r)))) <= (not(x in a) <= (not(x in q)))

for x in range(1, 1000):
    if ((not((x in q) <= ((x in p) or (x in r)))) <= (not(x in a) <= (not(x in q)))) is False:
        a.append(x)

print(len(a))