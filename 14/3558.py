def preobr_v_10(n, ss):
    n = str(n)[::-1]
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (ss ** i)
    return ans

for x in range(1, 10):
    a = preobr_v_10(101, x)
    b = preobr_v_10(101, x + 1)

    if a + 13 == b:
        print(x)
        break
