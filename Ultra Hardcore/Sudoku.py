
from brute_force import Brute_force_solve
from simple_elimination import simple_elimination
from hidden_single import hidden_single
class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        while True:
            hidden_singles = hidden_single(self.puzzle) 
            if hidden_singles > 0:     
                simple_elimination(self.puzzle)


            if self.is_solved():
                break
            
            if hidden_singles == 0 and self.is_unsolved_cells_exist():
                Brute_force_solve(self.puzzle)

        return self.puzzle

    def is_solved(self):
        return all(0 not in row for row in self.puzzle)

    def is_unsolved_cells_exist(self):
        return any(0 in row for row in self.puzzle)

    def print_board(self):
        """Ta funkcjia tworzy planszę sudoku"""
        print("-\t" * 13)
        for row in range(0, len(self.puzzle)):
            formatted_str = "|" + "\t"
            for col in range(0, len(self.puzzle[row])):
                if col in [3, 6]:
                    formatted_str += "|\t"
                formatted_str += str(self.puzzle[row][col]) + "\t"
            formatted_str += "|"
            print(formatted_str)
            if row in [2, 5]:
                print("-\t" * 13)
        print("-\t" * 13)

if __name__ == "__main__":
    puzzle =     [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9],
    ]
    sudoku = Sudoku(puzzle)
    print("Original Puzzle:")
    sudoku.print_board()
    sudoku.solve()
    print("=" * 31)
    print("Solved Puzzle:")
    sudoku.print_board()

