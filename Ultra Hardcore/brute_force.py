def Brute_force_solve(puzzle):
    empty_cell = find_empty_cell(puzzle)
    
    if not empty_cell:
        return True
        
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num
            if Brute_force_solve(puzzle):
                return True
            puzzle[row][col] = 0  
    return False  

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(board, row, col, num):
    return (
        not used_in_row(board, row, num) and
        not used_in_col(board, col, num) and
        not used_in_box(board, row - row % 3, col - col % 3, num)
    )

def used_in_row(board, row, num):
    return num in board[row]

def used_in_col(board, col, num):
    return num in [board[i][col] for i in range(9)]

def used_in_box(board, box_start_row, box_start_col, num):
    for i in range(3):
        for j in range(3):
            if board[i + box_start_row][j + box_start_col] == num:
                return True
    return False