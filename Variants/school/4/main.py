#2
# # ((x <= y) == w) or (not(y) and z)

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x <= y) == w) or (not(y) and z)):
#                     print(x, y, z, w)

#5 

# def preobr_v_ss(n, ss):
#     a = ''
#     while n > 0:
#         a += str(n % ss)
#         n //= ss
#     return a[::-1]


# def preobr(n):
#     f_n = preobr_v_ss(n, 5)
#     f_n_1 = f_n[::-1].lstrip('0')
#     return abs(int(f_n_1) - int(f_n))

# for n in range(1, 1000):
#     ans = preobr(n)
#     print(ans)
#     if ans == 100:
#         print(n)
#         break


# 8 

# def preobr_v_ss(n, ss):
#     a = ''
#     while n > 0:
#         a += str(n % ss)
#         n //= ss
#     return a[::-1]

print(f'{bin(255)[2:]}.{bin(255)[2:]}.{bin(0)[2:]}.{bin(0)[2:]}')
