from main_terminal import create_board, print_board

board = create_board(9, 9, 27)
print_board(board)

num = 0
for line in range(len(board)):
    for col in range(len(board[line])):
        if board[line][col] != 0:
            num += 1

print(num)