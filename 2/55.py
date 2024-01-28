# (a <= b) and ((a and b) <= not(c))

print("a b c")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if (a <= b) and ((a and b) <= (not(c))):
                print(a, b, c)
                