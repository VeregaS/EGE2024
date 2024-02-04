from sys import setrecursionlimit

setrecursionlimit(99999)
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + f(n - 1)
    

print(f(2024) - f(2021))