def dbl_linear(n):
    u = [1]
    x = 0
    y = 0
    while len(u) <= n:
        a = 2 * u[x] + 1
        b = 3 * u[y] + 1
        if a > b:
            u.append(b)
            y += 1
        elif a < b:
            u.append(a)
            x += 1
        else:
            u.append(a)
            x += 1
            y += 1
    return u[n]