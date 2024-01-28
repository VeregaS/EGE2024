def prevod_v_10(n, ss):
    n = str(n)[::-1]
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (ss ** i)
    return ans


for ss in range(1, 11):
    a = prevod_v_10(12, ss)
    b = prevod_v_10(13, ss)
    c = prevod_v_10(211, ss)
    
    if int(a) * int(b) == int(c):
        print(ss)
        break
