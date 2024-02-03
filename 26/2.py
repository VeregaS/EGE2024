f = open('26-1.txt').readlines()
f = [i.rstrip('\n') for i in f]
s, n = [int(i) for i in f[0].split()]
f[0] = None
f = sorted([int(i) for i in f if i is not None])


sum = 0
sum_counter = 0
max = f[-1]
for i in range(len(f)):
    if sum + f[i] <= s:
        sum += f[i]
        sum_counter += 1
    else:
        sum -= f[i - 1]
        break
    
    
for i in range(len(f)):
    if sum + f[i] > s:
        max = f[i - 1]
        
print(sum_counter, max)
