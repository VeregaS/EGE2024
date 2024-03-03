from itertools import product

s = open('24/2.txt').readline()
lenghts = []
bad = list("".join(i) for i in product('ABC', repeat=2))
counter = 1
for i in range(len(s) - 1):
    a = s[i] + s[i + 1]
    if a not in bad:
        counter += 1
    else:
        lenghts.append(counter)
        counter = 1

print(max(lenghts))