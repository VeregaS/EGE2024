# 19 cc:  98x79641 + 36x14 + 73x4

alph = '0123456789ABCDEFGHI'
ans = 0

def preob_v_10(n, ss):
    n = str(n)[::-1]
    ans = 0
    for i in range(len(n)):
        try:
            ans += int(n[i]) * (ss ** i)
        except:
            ans += alph.index(n[i]) * (ss ** i)
    return ans

for x in alph:
    a, b, c = f'98{x}79641', f'36{x}14', f'73{x}4'
    a_10, b_10, c_10 = preob_v_10(a, 19), preob_v_10(b, 19), preob_v_10(c, 19)
    if (a_10 + b_10 + c_10) % 18 == 0:
        ans = (a_10 + b_10 + c_10) // 18

print(ans)
