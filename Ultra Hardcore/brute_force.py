class BruteForceSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.found_number = False 

    def solve(self):
        empty_cell = self.find_empty_cell(self.puzzle)
        
        if not empty_cell:
            return True
            
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_valid_move(self.puzzle, row, col, num):
                self.puzzle[row][col] = num
                self.found_number = True  
                return True  

        return False  # No valid number found

    def find_empty_cell(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid_move(self, board, row, col, num):
        return (
            not self.used_in_row(board, row, num) and
            not self.used_in_col(board, col, num) and
            not self.used_in_box(board, row - row % 3, col - col % 3, num)
        )

    def used_in_row(self, board, row, num):
        return num in board[row]

    def used_in_col(self, board, col, num):
        return num in [board[i][col] for i in range(9)]

    def used_in_box(self, board, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if board[i + box_start_row][j + box_start_col] == num:
                    return True
        return False
