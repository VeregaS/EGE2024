s = list(int(i.rstrip('\n')) for i in open('17-4.txt').readlines())
counter = 0
m = []
for n in s:
    if n % 3 == 0 and n % 7 != 0 and n % 17 != 0 and n % 19 != 0 and n % 27 != 0:
        counter += 1
        m.append(n)
print(counter, max(m))
        