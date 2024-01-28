s = list(int(i.rstrip('\n')) for i in open('17-3.txt').readlines())
counter = 0
gip_sum = 0

for i in range(len(s) - 2):
    n = [s[i], s[i + 1], s[i + 2]]
    gip = n.pop(n.index(max(n)))

    if gip ** 2 == n[0] ** 2 + n[1] ** 2:
        counter += 1
        gip_sum += gip

print(counter, gip_sum)
