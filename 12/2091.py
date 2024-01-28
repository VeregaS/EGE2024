# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

a = '123' * 25 + '213' * 25


def func(n):
    while '13' in n or '32' in n or '12' in n:
        if '13' in n:
            n = n.replace('13', '31', 1)
        if '32' in n:
            n = n.replace('32', '23', 1)
        if '12' in n:
            n = n.replace('12', '21', 1)
    return n


ans = func(a)
print(ans[9], ans[69], ans[139], sep='')
