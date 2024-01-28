a = 9 ** 8 + 3 ** 5 - 9

a_3 = []
while a > 0:
    a_3.append(a % 3)
    a //= 3

print(a_3.count(2))
