# s = open('24/txts/test_24-5.txt').readline()
s = open('24/txts/24-5.txt').readline()

alph = [2, 3, 4, 5, 6, 7, 8, 9]
for i in alph:
    s = s.replace(f'{i}', '-')
for i in range(100, 0, -1):
    s = s.replace('-'*i, '-')
s = s.split('-')
ans = []
for elem in s:
    if len(elem) >= 2 and elem.count('1') >= 1 and elem.count('0') >= 1:
        elem = elem + '0'
        ans_1 = []
        count_len =  0
        last_was_0 = False
        last_was_1 = False
        for j in range(len(elem)):
            if elem[j] == '0':
                count_len += 1
                last_was_0 = True
            if elem[j] == '1' and ((last_was_0 is True) or (last_was_1 is True)) and elem[j + 1] == '0':
                count_len += 1
                ans_1.append(count_len)
                count_len = 0
                last_was_0 = False
                last_was_1 = False
            if elem[j] == '1' and ((last_was_0 is True) or (last_was_1 is True)):
                count_len += 1
        if len(ans_1) != 0:
            ans.append(max(ans_1))
print(s)
print(max(ans))