from fnmatch import fnmatch


def f(start, end, way):
    if start == end and (fnmatch(str(way), '?B*C??') is True):
        return 1   
    if start < end:
        return 0
    if start > end:
        return f(start - 2, end, str(way) + str('A')) + f(start // 2, end, str(way) + str('B')) + f(start - 3, end, str(way) + str('C'))
    

print(f(29, 2, str('')))
