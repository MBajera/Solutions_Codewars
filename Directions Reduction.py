def dirReduc(arr):
    op_dirs = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST"
    }
    i = 0
    while i < len(arr)-1:
        if op_dirs[arr[i]] == arr[i+1]:
            arr.pop(i)
            arr.pop(i)
            if i != 0:
                i -= 1
        else:
            i += 1
    return arr