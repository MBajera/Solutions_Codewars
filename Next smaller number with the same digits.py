from itertools import permutations

def next_smaller(n):
    poss_nums = []
    for elem in list(permutations(str(n))):
        to_check = "".join(elem)
        if to_check[0] != '0' and int(to_check) < n:
            poss_nums.append(int(to_check))
    return max(poss_nums) if len(poss_nums) > 0 else -1

#is solving problem but is to slow