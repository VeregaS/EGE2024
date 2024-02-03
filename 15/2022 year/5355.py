# ((x % 2 == 0) <= not((x % 3 == 0))) or ((x + a) >= 80)

for a in range(1, 1000):
    if all((((x % 2 == 0) <= (not((x % 3 == 0)))) or ((x + a) >= 80)) for x in range(1, 1000)) is True:
        print(a)
        break