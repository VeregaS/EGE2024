alph_ss = '0123456789ABCDEFGHIJKLM'

def preobr_v_10(n, ss):
    ans = 0
    n = str(n)[::-1]
    for i in range(len(n)):
        if str(n[i]) in alph_ss[:10]:
            ans += int(n[i]) * (ss ** i)
        else:
            ans += alph_ss.index(str(n[i])) * (ss ** i)
    return ans

for x in alph_ss:
    a = preobr_v_10(f'7{x}38596', 23)
    b = preobr_v_10(f'14{x}36', 23)
    c = preobr_v_10(f'61{x}7', 23)

    if (a + b + c) % 22 == 0:
        print((a + b + c) // 22)
        break