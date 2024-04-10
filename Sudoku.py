from solver import Solver

class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solver = Solver(self.puzzle)

    def solve(self):
        self.solver.solve()

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
    puzzle = [
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