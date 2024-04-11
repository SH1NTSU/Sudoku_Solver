
from helper_functions import SudokuHelper

def simple_elimination(puzzle):
    for iterations in range(0, 3):
        zones = SudokuHelper.extract_zones(puzzle)
        for zone in zones:
            if zone["type"] == "row":
                row = zone["position"]
                for col in range(0, 9):
                    SudokuHelper.insert_possibilities(puzzle, row, col)
            elif zone["type"] == "col":
                col = zone["position"]
                for row in range(0, 9):
                    SudokuHelper.insert_possibilities(puzzle, row, col)
            else:
                row_start, row_end, col_start, col_end = zone["position"]
                for row in range(row_start, row_end + 1):
                    for col in range(col_start, col_end + 1):
                        SudokuHelper.insert_possibilities(puzzle, row, col)
    return puzzle
