f = open('26/txts/26-139.txt').readlines()
f = [(i.rstrip('\n')).split() for i in f]
f = [[int(i) for i in j] for j in f]
n, k = f.pop(0)

f.sort(key=lambda x: [x[0], -x[1]])


ans_2 = 0
for i in range(len(f)):
    if f[i][1] == k:
        ans_2 += 1

a1 = 0
for i in range(len(f)):
    if f[i][0] == a1:
        f[i] = None
    else:
        a1 = f[i][0]
f = [i for i in f if i is not None]



second_el_1 = f[0][1]
max_l = 0
counter = 1

for i in range(1, len(f)):
    first_el_2 = f[i][0]
    second_el_2 = f[i][1]
    
    if first_el_2 <= second_el_1 + 1:
        if second_el_2 > max_l:
            max_l = second_el_2
            if max_l == k:
                    counter += 1
                    break
    else:
        counter += 1
        second_el_1 = max_l
        max_l = 0
        if first_el_2 <= second_el_1 + 1:
            if second_el_2 > max_l:
                max_l = second_el_2
                if max_l == k:
                    counter += 1
                    break

print(n - counter, ans_2)

