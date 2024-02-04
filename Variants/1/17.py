s = [int(i.rstrip('\n')) for i in open('Variants/1/17_9748.txt').readlines()]

maxs = []
for i in s:
    if str(i)[-2:] == '15':
        maxs.append(i)
max_15 = max(maxs)


ans = 0
summs = []
for i in range(len(s) - 2):
    n = [s[i], s[i + 1], s[i + 2]]
    summ = sum(n)
    if summ >= max_15:
        counter = 0
        for j in n:
            if len(str(j)) == 4 and str(j)[0] != '-':
                counter += 1
            elif len(str(j)) == 5 and str(j)[0] == '-':
                counter += 1
        if counter == 1:
            ans += 1
            summs.append(summ)
            
print(ans, max(summs))