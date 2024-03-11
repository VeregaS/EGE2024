# (x in q) <= ( ((x in p) == (x in q)) or ((not(x in p)) <= (x in a)) )

p = [i for i in range(55, 81)]
q = [i for i in range(20, 106)]

a = []
for x in range(10**3):
    if ((x in q) <= ( ((x in p) == (x in q)) or ((not(x in p)) <= (x in a)))) is False:
        a.append(x)

print(len(a))