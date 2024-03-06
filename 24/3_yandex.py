s = open('24/txts/3.txt').readline()
s = s.replace('4', 'a')
s = s.replace('3', 'e')
#yandex
n = '0123456789'
a = 'qwrtuiopsfhjklzcvbm'
for i in n:
    s = s.replace(i, '*')
for i in a:
    s = s.replace(i, '*')

print(s)
    