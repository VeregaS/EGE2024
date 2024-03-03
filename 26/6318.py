s = open('26/txts/26-112.txt')

banks_n, peoples = [int(i) for i in s.readline().split()]


a = []
for i in range(peoples):
    start, work_time = [int(i) for i in s.readline().split()]
    end = start + work_time
    a.append([start, end, work_time])
a.sort(key=lambda x: x[0])


banks = [0] * banks_n
banks_counter = [0] * banks_n
last_start = 0

for i in range(peoples):
    start, end, work_time = a[i]
    faind_bank = False
    
    for j in range(banks_n):
        if banks[j] <= start:
            if start <= 1440:
                banks_counter[j] += 1
                last_start = start
            banks[j] = end
            faind_bank = True
            break
            
    if faind_bank is False:
        min_index = banks.index(min(banks))
        min_start = banks[min_index]
        if min_start <= 1440:
            banks_counter[min_index] += 1
            last_start = min_start
        banks[min_index] = min_start + work_time
    

print(max(banks_counter), last_start)
