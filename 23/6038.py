from functools import lru_cache
from sys import setrecursionlimit

@lru_cache(None)
def f(start, end, last_h):
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        if last_h == 'NN':
            return f(start + 1, end, last_h + 'A') + f(start + 3, end, last_h + 'B') + f(start * 2, end, last_h + 'C')
        elif last_h[-1] == 'A':
            return f(start + 3, end, last_h + 'B') + f(start * 2, end, last_h + 'C')
        elif last_h[-1] == 'B':
            return f(start + 1, end, last_h + 'A') + f(start * 2, end, last_h + 'C')
        elif last_h[-1] == 'C':
            return f(start + 3, end, last_h + 'B') + f(start + 1, end, last_h + 'A')
        
    

setrecursionlimit(10**8)
print(f(5001, 45789, 1))