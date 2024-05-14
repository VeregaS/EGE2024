s = open('24/txts/6676.txt').readline()
s = s.rstrip('\n')
alph = '0123456789ABCDEF'
new_s = ''
last_was_bad = False
for i in s:
    if i in alph:
        new_s += i
        last_was_bad = False
    elif (i not in alph) and (last_was_bad is False):
        new_s += '_'
        last_was_bad = True

new_s = new_s.split('_')
ans = []
for n in new_s:
    int_n = -100
    try:
        int_n = int(n, 16)
    except:
        pass
    if int_n != -100:
        ans.append(int_n)

print(len(str(hex(max(ans))[2:])))