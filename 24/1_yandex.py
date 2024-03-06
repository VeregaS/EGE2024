s = open('24/txts/1.txt').readline()
bad = 'LISENOK'
lenghts = []
counter = 0
for elem in s:
    if elem not in bad:
        counter += 1
    else:
        lenghts.append(counter)
        counter = 0
print(max(lenghts))