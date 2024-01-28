a = '9' * 96


def func(n):
    while '22222' in n or '9999' in n:
        if '22222' in n:
            n = n.replace('22222', '99', 1)
        else:
            n = n.replace('9999', '2', 1)
    return n


print(func(a))
