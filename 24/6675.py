s = open('24/txts/24-263.txt').readline()
new_s = ''
for n in s:
    if n != 'Y':
        new_s += '_'
    else:
        new_s += 'Y'
print(new_s)