def persistence(n):
    counter = 0
    while len(str(n)) != 1:
        new_n = 1
        for dig in str(n):
            new_n *= int(dig)
        n = new_n
        counter += 1
    return counter