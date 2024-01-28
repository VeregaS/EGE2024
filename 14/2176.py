a = 49 ** 12 - 7 ** 10 + 7 ** 8 - 49

def preobr_v_ss(n, ss):
    ans = []
    while n > 0:
        ans.append(str(n % ss))
        n //= ss
    return ''.join(ans[::-1])

print(preobr_v_ss(a, 7).count('6'))
