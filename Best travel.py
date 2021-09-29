def choose_best_sum(t, k, ls):
    import itertools
    posib = [sum(elem) for elem in list(itertools.combinations(ls,k)) if sum(elem)<=t]
    return max(posib) if posib else None