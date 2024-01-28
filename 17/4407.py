s = list(int(i.rstrip('\n')) for i in open('17-4.txt').readlines())
counter = 0
sumi2 = 10**8
for i in range(len(s) - 1):
    sumi = s[i] + s[i + 1]
    if (99 < sumi < 1000) and (sumi % 10 > (sumi // 10) % 10):
        counter += 1
        if sumi < sumi2:
            sumi2 = sumi
print(counter, sumi2)
