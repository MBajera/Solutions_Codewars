table = [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
         [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
         [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
         [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
         [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
         [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
         [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
         [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
         [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]


def sudoku(puzzle):
    while any(0 in sublist for sublist in puzzle):
        for x, row in enumerate(puzzle):
            for y, num in enumerate(row):
                if num == 0:
                    poss_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    square = []
                    for sublist in table:
                        if [x, y] in sublist:
                            square = sublist
                    for cord in square:
                        if puzzle[cord[0]][cord[1]] in poss_nums:
                            poss_nums.remove(puzzle[cord[0]][cord[1]])
                    for num_r in row:
                        if num_r in poss_nums:
                            poss_nums.remove(num_r)
                    for num_c in range(9):
                        if puzzle[num_c][y] in poss_nums:
                            poss_nums.remove(puzzle[num_c][y])
                    if len(poss_nums) == 1:
                        puzzle[x][y] = poss_nums[0]
    return puzzle
