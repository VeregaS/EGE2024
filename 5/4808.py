# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(n):
    s1 = 0
    s2 = 0
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            s1 += int(n[i])
        if (i + 1) % 2 == 0:
            s2 += int(n[i])
    return abs(s1 - s2)


for n in range(1, 100000000):
    if func(str(n)) == 29:
        print(n)
        break
        