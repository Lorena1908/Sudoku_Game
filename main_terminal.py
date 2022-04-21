import random

def print_board(board):
    for line in range(len(board)):
        print(board[line])


def board_full(board):
    # Check if the board is full
    for line in range(len(board)):
        for column in range(len(board[0])):
            if board[line][column] == 0:
                return False
    return True


def check_squares(board, line_pos, col_pos, line_offset, col_offset):
    # Check for equal numbers in the same square
    for line in range(3):
        line += line_offset
        
        for col in range(3):
            col += col_offset
            
            if board[line][col] == board[line_pos][col_pos] and line != line_pos and col != col_pos:
                return False
    return True


def check_line_and_col(board, line_pos, col_pos):
    # Check for equal numbers in the same line
    for col in range(len(board[line_pos])):
        if board[line_pos][col] == board[line_pos][col_pos] and col != col_pos:
            return False
    
    # Check for equal numbers in the same column
    for line in range(len(board)):
        if board[line][col_pos] == board[line_pos][col_pos] and line != line_pos:
            return False
    return True 


def generate_offset(line, col):
    # Generate the line and column offsets for the check_squares() function
    if 0 <= line <= 2:
        line_offset = 0
    elif 3 <= line <= 5:
        line_offset = 3
    elif 6 <= line <= 8:
        line_offset = 6
    
    if 0 <= col <= 2:
        col_offset = 0
    elif 3 <= col <= 5:
        col_offset = 3
    elif 6 <= col <= 8:
        col_offset = 6
    return line_offset, col_offset


def check_winning(board):
    # Checks winning for every position in the board
    for line in range(len(board)):
        for col in range(len(board[0])):
            line_offset, col_offset = generate_offset(line, col)
            
            if not(check_line_and_col(board, line, col)) or not(check_squares(board, line, col, line_offset, col_offset)):
                return False
    return True


def create_board(rows, columns, total_num):
    # Creates a board with total_num amount of random numbers. The random 
    # numbers must not have an equal one in the same line, column or square
    board = [[0 for _ in range(rows)] for _ in range(columns)]

    num = 0
    while num < total_num:
        line = random.randrange(rows)
        col = random.randrange(rows)

        if board[line][col] != 0:
            continue

        num_board = random.randrange(1, rows+1)
        line_offset, col_offset = generate_offset(line, col)

        board[line][col] = num_board

        if not(check_line_and_col(board, line, col)) or not(check_squares(board, line, col, line_offset, col_offset)):
            board[line][col] = 0
            continue

        num += 1
    return board


def main():
    # Main function of the game
    rows = 9
    board = create_board(rows, rows, 18)
    run = True
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
        if board[line-1][col-1] == 0:
            board[line-1][col-1] = num
        else:
            print("Invalid Position")

        print_board(board)

        # Check if the board is full and if the player won
        if board_full(board):
            if check_winning(board):
                print("WON")
            else:
                print("LOST")
            break

if __name__ == '__main__':
    main()