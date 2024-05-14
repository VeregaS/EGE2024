from fnmatch import fnmatch

s = [i.rstrip('\n') for i in open('24/txts/24-3.txt').readlines()]
counter = 0
for i in s:
    for j in range(len(i) - 3):
        a = i[j:j+4]
        if fnmatch(a, 'Z*RO'):
            print(a)
            counter += 1
            break
print(counter)