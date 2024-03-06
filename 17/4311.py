s = list(int(i.rstrip('\n')) for i in open('17/txts/17-2.txt').readlines())
m = []

for n in s:
    if n % 13 == 4 and n % 8 == 1:
        m.append(n)

print(max(m), sum(m))