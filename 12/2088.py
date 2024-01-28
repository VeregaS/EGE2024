a = '1' * 44 + '2' * 21


def func(n):
    while '111' in n:
        n = n.replace('111', '2', 1)
        n = n.replace('22', '1', 1)
    return n


print(func(a))
