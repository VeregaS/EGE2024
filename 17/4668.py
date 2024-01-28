s = list(int(i.rstrip('\n')) for i in open('17-5.txt').readlines())
counter = 0
sumi = []

sr_ar = sum(s) / len(s)

for i in range(len(s) - 1):
    n = [s[i], s[i + 1]]
    if min(n) < sr_ar:
        if ''.join([str(j) for j in n]).count('7') > 0:
            counter += 1
            sumi.append(sum(n))

print(counter, min(sumi))