from functools import lru_cache
a = []

@lru_cache(None)
def f(start, end, counter):
    if start == end:
        a.append(counter)
        return 1
    if start > end:
        return 0 
    if start < end:
        return f(start + 1, end, counter + 1) + f(start + 5, end, counter + 1) + f(start * 3, end, counter + 1)
    

f(1, 227, 0)
print(min(a))