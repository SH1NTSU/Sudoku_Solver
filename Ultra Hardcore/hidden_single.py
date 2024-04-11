
from helper_functions import SudokuHelper

def hidden_single(puzzle):
    def find_only_number_in_group(group, number):
        count = 0
        removed = 0
        cell_to_clean = (-1, -1)
        for cell_row, cell_col in group:
            if puzzle[cell_row][cell_col] == 0:
                row_elements = SudokuHelper.get_zone_elements(puzzle, "row", cell_row, cell_col)
                col_elements = SudokuHelper.get_zone_elements(puzzle, "col", cell_row, cell_col)
                square_elements = SudokuHelper.get_zone_elements(puzzle, "square", cell_row, cell_col)
                numbers = [num for num in range(1, 10)]
                possibilities = [i for i in range(1, 10)]
                for possibility in numbers:
                    if (possibility in row_elements) or (possibility in col_elements) or (possibility in square_elements):
                        possibilities.remove(possibility)
                if number in possibilities:
                    count += 1
                    cell_to_clean = (cell_row, cell_col)
        if count == 1 and cell_to_clean != (-1, -1):
            row, col = cell_to_clean
            puzzle[row][col] = number
            removed = 1
        return removed

    count = 0
    zones = SudokuHelper.extract_zones(puzzle)
    for number in range(1, 10):
        for zone in zones:
            if zone["type"] == "row":
                for col in range(9):
                    count += find_only_number_in_group([(zone["position"], col) for col in range(9)], number)
            elif zone["type"] == "col":
                for row in range(9):
                    count += find_only_number_in_group([(row, zone["position"]) for row in range(9)], number)
            else:
                row_start, row_end, col_start, col_end = zone["position"]
                group = [(row, col) for row in range(row_start, row_end + 1) for col in range(col_start, col_end + 1)]
                count += find_only_number_in_group(group, number)
    return count
