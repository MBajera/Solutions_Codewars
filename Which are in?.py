def in_array(array1, array2):
    return sorted(set([elem for elem in array1 if elem in " ".join(array2)]))