s = [str(i).rstrip('\n') for i in list(open('Variants/1/9.txt').readlines())]

ans = 0
for line in s:
    line = line.split()
    l = [i for i in set(line)]
    if len(l) == 5:
        c_1 = 0
        c_3 = 0
        l_3 = ''
        for i in l:
            if line.count(i) == 1:
                c_1 += 1
            if line.count(i) == 3:
                c_3 += 1
                l_3 = i
        if c_3 == 1 and c_1 == 4:
            l.remove(l_3)
            l = [int(i) for i in l]
            sr_ar = sum(l) / len(l)
            if sr_ar <= float(l_3):
                print(line)
                ans += 1
                
print(ans)
        
