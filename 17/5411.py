s = [int(i.rstrip('\n')) for i in open('17/txts/17-341.txt').readlines()]

counter = 0
a = []
sr_ar = sum(s) / len(s)
for i in range(1, len(s) - 3):
    befor_past = s[i - 1] * s[i + 2]
    para = s[i] * s[i + 1]
    if para > befor_past:
        if s[i] > sr_ar or s[i + 1] > sr_ar:
            counter += 1
            a.append(s[i] + s[i + 1])

print(max(a), counter)