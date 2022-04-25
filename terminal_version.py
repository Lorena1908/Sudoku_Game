from board import Board

def main():
    # Main function of the game
    board = Board(9,9)
    run = True
    board.print_board()

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
        if board.grid[line-1][col-1] == 0:
            board.grid[line-1][col-1] = num
        else:
            print("Invalid Position")

        board.print_board()

        # Check if the board is full and if the player won
        if board.board_full(board.grid):
            if board.check_winning():
                print("WON!")
            else:
                print("LOST!")
            run = False

if __name__ == '__main__':
    main()