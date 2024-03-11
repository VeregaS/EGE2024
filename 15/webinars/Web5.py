d = [i for i in range(17, 59)]
c = [i for i in range(29, 81)]

a = []

for x in range(1, 1000):
    if ((x in d) <= ((not(x in c) and (not(x in a))) <= (not(x in d)))) is False:
        a.append(x)

print(len(a))
