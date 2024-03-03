s = open('26/txts/26-125.txt')
# s = open('26/txts/6611_example.txt')

n_gnoms, n_chans = [int(i) for i in s.readline().split()]


# 2 mana -> 1 potion (1 min)
a = []
for i in range(n_gnoms):
    start, mana = [int(i) for i in s.readline().split()]
    a.append([start, mana])

a.sort()


chans = [0] * n_chans
gnoms = [0] * n_gnoms

for i in range(n_gnoms):
    start, mana = a[i]
    is_waiting = True
    if mana > 1:
        for j in range(n_chans):
            if chans[j] <= start:
                work_time = mana // 2
                chans[j] = start + work_time + 2 
                
                if start <= 1440:
                    if work_time + start <= 1440:
                        gnoms[i] = mana // 2
                    else:
                        over = start + work_time - 1440
                        done = work_time - over 
                        gnoms[i] = done
                    is_waiting = False
                break
        
        if is_waiting == True:
            min_index = chans.index(min(chans))
            min_start = chans[min_index]
            work_time = mana // 2
            chans[min_index] = min_start + work_time + 2
            
            
            if min_start <= 1440:
                if work_time + min_start <= 1440:
                    gnoms[i] = mana // 2
                else:
                    over = min_start + work_time - 1440
                    done = work_time - over 
                    gnoms[i] = done
                
        
print(sum(gnoms), max(gnoms))
