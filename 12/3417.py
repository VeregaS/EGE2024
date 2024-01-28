a = '4' + '5' * 90


def func(n):
    while '25' in n or '355' in n or '4555' in n:
        if '25' in n:
            n = n.replace('25', '3', 1)
        if '355' in n:
            n = n.replace('355', '4', 1)
        if '4555' in n:
            n = n.replace('4555', '2', 1)
    return n


print(func(a))
