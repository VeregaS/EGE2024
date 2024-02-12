arf = 36 ** 27 + 6 ** 18 - 19

def perevod(n, ss):
    ans = ''
    while n > 0:
        ans += str(n % ss)
        n //= ss
    return ans[::-1]

print(perevod(arf, 6).count('0'))