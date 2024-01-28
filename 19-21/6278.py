def f(s, n):
    if str(s)[-1] == '8':
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s + 1, n - 1), f(s + 3, n - 1), f(s + 11, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)



a_19, a_20, a_21 = [], [], []

for s in range(10, 100):
    if str(s)[-1] != '8':
        # 19
        if not f(s, 1) and f(s, 2):
            a_19.append(s)
        # 20
        if not f(s, 1) and f(s, 3):
            a_20.append(s)
        # 21
        if f(s, 4) and not f(s, 2):
            a_21.append(s)
            
print('19)', min(a_19))
print('20)', len(a_20))
print('21)', min(a_21), max(a_21))