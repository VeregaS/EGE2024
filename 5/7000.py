ans = 0

def func(N):
    sum_ = sum([int(i) for i in str(N)])
    bin_sum = bin(sum_)[2:]
    if bin_sum.count('1') % 2 == 0:
        bin_r = f"1{bin_sum}00"
    else:
        bin_r = f"10{bin_sum}1"
    r = int(bin_r, 2)
    return r
    
for N in range(100000000, 1000000000):
    if func(N) == 21:
        ans += 1
        
print(ans)


r = 21
b = bin(r)[2:]
bin_sum = 10
sum = int('10', 2)
print(sum)
# 100_000_001 => 8 (100_000_010, 100_000_100, ....)
# 200_000_000 => 1
# => 8+1 = 9
