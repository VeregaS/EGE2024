s = list(int(i.rstrip('\n')) for i in open('17/txts/17-6.txt').readlines())
counter = 0
sumi = []

sr_ar = sum(s) / len(s)

for i in range(len(s) - 1):
    n = [s[i], s[i + 1]]
    if min(n) < sr_ar:
        if str(s[i]).count('5') == 0 or str(s[i + 1]).count('5') == 0:
            counter += 1
            sumi.append(sum(n))

print(counter, min(sumi))