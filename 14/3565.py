ans = 0
for x in range(64, 100000):
    octo = oct(x)[2:]
    hexx = hex(x)[2:]
    if hexx[0] == '3' and hexx[2] == '9' and len(hexx) == 3:
        if octo[0] == '1'and len(octo) == 3:
            ans += 1
print(ans)
