from random import randrange, shuffle
import copy

# These three functions: create_board_and_solution, generate_not_solved_board and 
# generate_solved_board I adapted from https://www.101computing.net/sudoku-generator-algorithm/

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


def generate_quadrant_meta(line, col):
    # Generate the line and column offsets for the quadrant_not_equal() function
    if 0 <= line <= 2 and 0 <= col <= 2:
        start_range, end_range = 0, 3
        start_pos, end_pos = 0, 3
    elif 0 <= line <= 2 and 3 <= col <= 5:
        start_range, end_range = 0, 3
        start_pos, end_pos = 3, 6
    elif 0 <= line <= 2 and 6 <= col <= 8:
        start_range, end_range = 0, 3
        start_pos, end_pos = 6, 9
    elif 3 <= line <= 5 and 0 <= col <= 2:
        start_range, end_range = 3, 6
        start_pos, end_pos = 0, 3
    elif 3 <= line <= 5 and 3 <= col <= 5:
        start_range, end_range = 3, 6
        start_pos, end_pos = 3, 6
    elif 3 <= line <= 5 and 6 <= col <= 8:
        start_range, end_range = 3, 6
        start_pos, end_pos = 6, 9
    elif 6 <= line <= 8 and 0 <= col <= 2:
        start_range, end_range = 6, 9
        start_pos, end_pos = 0, 3
    elif 6 <= line <= 8 and 3 <= col <= 5:
        start_range, end_range = 6, 9
        start_pos, end_pos = 3, 6
    elif 6 <= line <= 8 and 6 <= col <= 8:
        start_range, end_range = 6, 9
        start_pos, end_pos = 6, 9
    
    quadrant_meta = {
        'start_range': start_range,
        'end_range': end_range,
        'start_pos': start_pos,
        'end_pos': end_pos,
    }
    
    return quadrant_meta


def quadrant_not_equal(board, line, col, number):
    # Check for equal numbers in the same quadrant
    square = []
    quadrant_meta = generate_quadrant_meta(line, col)
    
    for line in range(quadrant_meta['start_range'], quadrant_meta['end_range']):
        square.append(board[line][quadrant_meta['start_pos']:quadrant_meta['end_pos']])
    
    for line in square:
        if number in line:
            return False
    return True


def line_col_not_equal(board, line_pos, col_pos, number):
    column = []
    # Check for equal numbers in the same line
    if number in board[line_pos]:
        return False
    
    for line in range(len(board)):
        column.append(board[line][col_pos])

    # Check for equal numbers in the same column
    if number in column:
        return False
    return True 


def check_winning(board, solution):
    for line in range(len(board)):
        for col in range(len(board[line])):
            if board[line][col] != solution[line][col]:
                return False
    return True


def generate_solved_board(board):
    numbers = [1,2,3,4,5,6,7,8,9]
    shuffle(numbers) 
    for i in range(0,81):
        line = i // 9
        col = i % 9
        # Get the next empty cell
        if board[line][col] == 0:
            shuffle(numbers) 
            for value in numbers:
                # Check a number fits into the current cell according to sudoku's rules
                if line_col_not_equal(board, line, col, value) and quadrant_not_equal(board, line, col, value):
                    board[line][col] = value
                    if board_full(board): # If the board is full
                        return True
                    else:
                        if generate_solved_board(board): # Call the function again
                            return True
            # If it goes though all numbers and none fit the cell, then it's not possible to solve
            # this sudoku board, so get out of this loop, make the current cell 0, and check if
            # in the previous cell there is another number other than the current one that fits
            # the cell according to the rules. If it finds another number that fits the current cell,
            # go on checking the next cells normally, otherwise, make the previous cell 0 and check do it 
            # all over again.
            break
    board[line][col] = 0 


def generate_not_solved_board(board):
    global counter
    for i in range(0,81):
        line = i // 9
        col = i % 9
        # Find next empty cell
        if board[line][col] == 0:
            for value in range (1,10):
                # Check that this value has not already be used on this row, column or quadrant
                if line_col_not_equal(board, line, col, value) and quadrant_not_equal(board, line, col, value):
                    board[line][col] = value
                    if board_full(board): # if the board is full
                        counter += 1 # add 1 to the solutions counter 
                        break
                    else:
                        if generate_not_solved_board(board):
                            return True
            break
    board[line][col] = 0


def create_board_and_solution(rows, columns):
    global counter
    attempts = 5 # To increase the dificulty increse the attempts number
    board = [[0 for _ in range(rows)] for _ in range(columns)]
    generate_solved_board(board)
    solution = copy.deepcopy(board)

    while attempts > 0:
        line, col = randrange(rows), randrange(columns)
        while board[line][col] == 0:
            line, col = randrange(rows), randrange(columns)
        
        backup_value = board[line][col]
        board[line][col] = 0

        board_copy = copy.deepcopy(board)
        counter = 0
        generate_not_solved_board(board_copy)

        if counter != 1:
            board[line][col] = backup_value
            attempts -= 1
    
    return board, solution


def main():
    # Main function of the game
    rows, columns = 9, 9
    board, solution = create_board_and_solution(rows, columns)
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
            if check_winning(board, solution):
                print("WON!")
            else:
                print("LOST!")
            run = False

if __name__ == '__main__':
    main()