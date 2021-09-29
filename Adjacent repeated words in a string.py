def count_adjacent_pairs(st):
    splited = list(filter(None, st.lower().split(' ')))
    counter = 0
    if len(splited) > 0:
        last_added = ''
        for i in range(1,len(splited)):
            if splited[i] == splited[i-1] and splited[i] != last_added:
                last_added = splited[i]
                counter += 1
    return counter
