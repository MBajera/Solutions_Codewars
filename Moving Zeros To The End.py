def move_zeros(array):
    count = array.count(0)
    array = [value for value in array if value != 0]
    return array + [0 for x in range(count)]
