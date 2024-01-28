#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


from itertools import permutations
lib = '0123456789ABCDEF'
num = '0123456789'

numbers = permutations(lib, 16)
ans = 0

for number in numbers:
    number = ''.join(number)
    n_set = set(number) 
    if len(n_set) == len(number):
        num_counter = 0
        for i in number:
            if i in num:
                num_counter += 1
        if num_counter == 4:
            if int(number[0], 16) % 2 != int(number[1], 16) % 2 and int(number[1],16) % 2 != int(number[2],16) % 2:
                print(ans)
                ans += 1

print(ans)
