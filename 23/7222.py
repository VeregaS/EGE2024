# from sys import setrecursionlimit
# from functools import *

# setrecursionlimit(999999)
# @lru_cache(None)
# def f(s, e):
#     if s == e:
#         return 1
#     if s > e:
#         return 0
#     return f(s + 1, e) + f(s + int(str(s)[0]), e) + f(s + int(str(s)[-1]), e)

    
# print(f(82, 95) * f(95, 103) * f(103, 124))
