def preobr_v_ss(n, ss):
    ans = []
    while n > 0:
        ans.append(str(n % ss))
        n //= ss
    return ''.join(ans[::-1])


for x in range(1, 10000000):
    x_16 = hex(x)[2:]
    x_8 = oct(x)[2:]
    x_4 = preobr_v_ss(x, 4)
    x_2 = bin(x)[2:]
    if len(x_16) == 2:
        if len(x_8) == 3:
            if len(x_4) == 4:
                if len(x_2) == 8:
                    if x_16[0] == 'e' and x_8[1] == '5' and x_4[-1] == '1' and x_2[5] == '1':
                        print(x)
                        break
