from itertools import product

v = list(product('123', repeat=4))
v = [''.join(i) for i in v]

a = set()
for i in v:
    current_number = 1
    for j in i:
        if j == '1':
            current_number += 1
        if j == '2':
            current_number += 5
        if j == '3':
            current_number *= 3
    a.add(current_number)
print(len(a))
