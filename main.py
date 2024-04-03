import random

all_houses = [[(i, j) for j in range(9)] for i in range(9)] + \
                [[(j, i) for j in range(9)] for i in range(9)] + \
                [[(i + j, i) for i in range(9)] for j in range(9)] + \
                [[(i, i + j) for i in range(9)] for j in range(9)] + \
                [[(i + j, i - j) for i in range(9)] for j in range(9)] + \
                [[(i, 8 - i + j) for i in range(9)] for j in range(9)]

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_sudoku(board):
    row, col = find_empty_location(board)
    if row == -1 and col == -1:
        return True
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def csp_list(inp):

    perm = []

    def append_permutations(sofar):
        nonlocal inp
        for n in inp[len(sofar)]:
            if len(sofar) == len(inp) - 1:
                perm.append(sofar + [n])
            else:
                append_permutations(sofar + [n])

    append_permutations([])

    for i in range(len(perm))[::-1]:
        if len(perm[i]) != len(set(perm[i])):
            del perm[i]

    out = []
    for i in range(len(inp)):
        out.append([])
        for n in range(10):
            for p in perm:
                if p[i] == n and n not in out[i]:
                    out[i].append(n)
    return out


def csp(s):
    count = 0
    for group in all_houses:
        house = []
        for cell in group:
            house.append(s[cell])
        house_csp = csp_list(house)
        if house_csp != house:
            for i in range(len(group)):
                if s[group[i]] != house_csp[i]:
                    count += len(s[group[i]]) - len(house_csp[i])
                    s[group[i]] = house_csp[i]
    return count


def generate_sudoku():

    board = [[(i * 3 + i // 3 + j) % 9 + 1 for j in range(9)] for i in range(9)]

    for i in range(0, 9, 3):
        random.shuffle(board[i:i+3])

    board = [[board[j][i] for j in range(9)] for i in range(9)]

    for i in range(0, 9, 3):
        random.shuffle(board[i:i+3])

    for _ in range(random.randint(45, 55)):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
    return board

random_sudoku_board = generate_sudoku()
print("Random Sudoku puzzle:")
print_board(random_sudoku_board)

if solve_sudoku(random_sudoku_board):
    print("\nSolved Sudoku puzzle:")
    print_board(random_sudoku_board)
else:
    print("\nNo solution exists.")



