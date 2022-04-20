from ctypes import sizeof


def create_board(rows, columns):
    return [[0 for _ in range(rows)] for _ in range(columns)]

def print_board(board):
    for line in range(len(board)):
        print(board[line])

def board_full(board):
    for line in range(len(board)):
        for column in range(len(board[0])):
            if board[line][column] == 0:
                return False
    return True

def check_winning(board, line_pos, col_pos):
    # Check for equal numbers in the same line
    for col in range(len(board[line_pos])):
        if board[line_pos][col] == board[line_pos][col_pos] and col != col_pos:
            return False
    
    # Check for equal numbers in the same column
    for line in range(len(board)):
        if board[line][col_pos] == board[line_pos][col_pos] and line != line_pos:
            return False
    return True        

# board = [
#     [0,3,4,6,7,8,9,1,2],
#     [6,7,2,1,9,5,3,4,8],
#     [1,9,8,3,4,2,5,6,7],
#     [8,5,9,7,6,1,4,2,3],
#     [4,2,6,8,5,3,7,9,1],
#     [7,1,3,9,2,4,8,5,6],
#     [9,6,1,5,3,7,2,8,4],
#     [2,8,7,4,1,9,6,3,5],
#     [3,4,5,2,8,6,1,7,9],
# ]

rows = 9
board = create_board(rows, rows)
run = True
won = True
print_board(board)

# Main game loop
while run:
    # Ask for player input
    line = int(input("Enter a line: "))

    if (line == 0):
        run = False
        continue

    col = int(input("Enter a column: "))
    num = int(input("Enter a number: "))

    # Add the number to the board
    board[line-1][col-1] = num

    full = board_full(board)

    print_board(board)

    if full:
        # Checks winning for every position in the board
        for line in range(len(board)):
            for col in range(len(board[0])):
                if not(check_winning(board, line, col)):
                    won = False
                    break
        if won:
            print("WON")
        else:
            print("LOST")
        break
    
