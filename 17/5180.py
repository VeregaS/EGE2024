s = [int(i.rstrip('\n')) for i in open('17/txts/17-304.txt').readlines()]

counter = 0
max_sum = []
min_elem = min(s)

for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) % min_elem == 0:
        sum_oct_1 = sum([int(j) for j in oct(s[i])[2:]])
        sum_oct_2 = sum([int(j) for j in oct(s[i + 1])[2:]])
        if (s[i] % sum_oct_2 == 0 and s[i + 1] % sum_oct_1 != 0) or (s[i + 1] % sum_oct_1 == 0 and s[i] % sum_oct_2 != 0):
            counter += 1
            max_sum.append(s[i] + s[i + 1])

print(counter, max(max_sum))