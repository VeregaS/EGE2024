from fnmatch import fnmatch

for i in range(10**4):
    if fnmatch(str(i), '*2?2'):
        print(i)