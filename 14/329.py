def preobr_v_10(number, ss):
    number = number[::-1]
    ans = 0
    for i in range(len(number)):
        ans += int(number[i]) * (ss ** i)
    return ans



def preobr_v_ss(n, ss):
    ans = []
    while n > 0:
        ans.append(str(n % ss))
        n //= ss
    return ''.join(ans[::-1])

print(preobr_v_ss(n=(preobr_v_10('120', 7) - preobr_v_10('60', 8)), ss=6))
