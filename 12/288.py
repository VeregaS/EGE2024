a = '8' * 18 + '5' * 3


def func(n):
    while '555' in n or '888' in n:
        if '555' in n:
            n = n.replace('555', '8', 1)
        while '888' in n:
            n = n.replace('888', '5', 1)
        if '555' in n:
            n = n.replace('555', '8', 1)
    return n

print(func(a))
