s = list(int(i.rstrip('\n')) for i in open('17-303.txt').readlines())
counter = 0
m1 = []
i1 = 0
for i in s:
    for x in range(1, 25):
        if x ** 3 == i:
            if i > i1:
                i1 = i

for i in range(len(s) - 2):
    n = [s[i], s[i + 1], s[i + 2]]
    a = abs(i1 - sum(n))
    if a % 2 == 0:
        if (a ** (0.5)) == int(a ** (0.5)):
            m1.append(n)

m1 = sorted(m1, key=lambda x: sum(x), reverse=True)
a = m1[0]
b = a.pop(a.index(max(a)))
a = [str(i) for i in a]
print(len(m1), eval('*'.join(a)))

        

