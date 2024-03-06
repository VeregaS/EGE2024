ans = set()

def f(start,counter):
    if counter == 4:
        ans.add(start)
        return 0
    return f(start * 3, counter + 1) + f(start + 2, counter + 1)

f(1, 0)
print(len(ans))



