def f(n):
    while '72' in n or '522' in n or '2222' in n:
        if '72' in n:
            n = n.replace('72', '2', 1)
        if '522' in n:
            n = n.replace('522', '27', 1)
        if '2222' in n:
            n = n.replace('2222', '5', 1)
    return n

for s in range(4, 10000):
    n = '5' + '2' * s
    res = f(n)
    sum_ = sum([int(i) for i in res])    
    if sum_ == 63:
        print(s)
        break
