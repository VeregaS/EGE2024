s = open('26/txts/26-111.txt')

kamers_colvo = int(s.readline())
passengers = int(s.readline())

a = []

for i in range(passengers):
    time = [int(j) for j in s.readline().split()]
    start, end = time[0], time[1]
    a.append([start, end])

a.sort()

kamers = [0] * kamers_colvo

counter = 0
last_kam = 0

for i in range(passengers):
    start, end = a[i][0], a[i][1]
    for j in range(kamers_colvo):
        if kamers[j] < start:
            kamers[j] = end
            counter += 1
            last_kam = j + 1
            break

print(counter, last_kam)
