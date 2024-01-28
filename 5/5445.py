# Интересное задание !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def func(n):
    n = n[::-1]
    preobr = []
    chet = []
    for i in range(len(n)):
        if i % 2 != 0:
            new_i = str(int(n[i]) * 2)
            if len(new_i) == 2:
                new_i_ = 0
                for j in new_i:
                    new_i_ += int(j)
                new_i = new_i_
            preobr.append(int(new_i)) 
        else:
            chet.append(int(n[i]))
    return (sum(preobr) + sum(chet))


for n in range(1234567891011122, 9999999999999999):
    if (func(str(n)) % 10 == 0) is True:
        print(str(n)[8:])
        break
