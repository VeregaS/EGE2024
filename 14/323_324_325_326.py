def preobr_v_ss(n, ss):
    ans = []
    while n > 0:
        ans.append(str(n % ss))
        n //= ss
    return str(''.join(ans[::-1]))

for ss in range(3, 10):
    if len(preobr_v_ss(30, ss)) == 3:
        print(ss)
        break
