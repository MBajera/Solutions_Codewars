def chess_board_cell_color(cell1, cell2):
    cells = [cell1, cell2]
    for cell in cells:
        if cell[0] in "ACEG":
            cells[cells.index(cell)] = (1 + int(cell[1])) % 2
        else:
            cells[cells.index(cell)] = int(cell[1]) % 2
    return cells[0] == cells[1]