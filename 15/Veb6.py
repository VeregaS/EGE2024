p = [i for i in range(3, 14)]
q = [i for i in range(12, 23)]

a = [i for i in range(1, 100)]

# ((x in a) <= (x in p)) or (x in q)

for x in range(1, 1000):
    if (((x in a) <= (x in p)) or (x in q)) is False:
        a.remove(x)
        
print(a[-1] - a[0]) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!