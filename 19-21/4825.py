def f(s, m, last_h):
    if s >= 43:
        return m % 2 == 0
    if m == 0:
        return 0
    if last_h == "":
        h = [f(s + 1, m - 1, '+1'), f(s + 2, m - 1, '+2'), f(s * 2, m - 1, '*2')]
    if last_h == "+1":
        h = [f(s + 2, m - 1, '+2'), f(s * 2, m - 1, '*2')]
    if last_h == "+2":
         h = [f(s + 1, m - 1, '+1'), f(s * 2, m - 1, '*2')]
    if last_h == "*2":
         h = [f(s + 1, m - 1, '+1'), f(s + 2, m - 1, '+2')]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('19) ', [s for s in range(1, 43) if f(s, 2, "") and not f(s, 1, "")])
print('20) ', [s for s in range(1, 43) if not f(s, 1, "") and f(s, 3, "")])
print('21) ', [s for s in range(1, 43) if f(s, 4, "") and not f(s, 2, "")])
