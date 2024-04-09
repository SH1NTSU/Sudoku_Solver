class Sudoku:
    def __init__(self, board) -> None:
       self.board = board
    
    def solve(self):
        pass
        
    def print_board(self):
        print("-\t" * 13)
        for row in range(0, len(self.board)):
            formatted_str = "|" + "\t"
            for col in range(0, len(self.board[row])):
                if col in [3, 6]:
                    formatted_str += "|\t"
                formatted_str += str(self.board[row][col]) + "\t"
            formatted_str += "|"
            print(formatted_str)
            if row in [2, 5]:
                print("-\t" * 13)
        print("-\t" * 13)

    
if __name__ == "__main__":
    puzzle = [
        [8, 7, 6, 9, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 6, 0, 0, 0],
        [0, 4, 0, 3, 0, 5, 8, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 1, 0],
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 4, 0, 3, 0, 6],
        [0, 2, 9, 0, 0, 0, 0, 0, 8],
        [0, 0, 4, 6, 9, 0, 1, 7, 3],
        [0, 0, 0, 0, 0, 1, 0, 0, 4]
    ]
    s = Sudoku(puzzle)
    print('=' * 50)
    s.print_board()
