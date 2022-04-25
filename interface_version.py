import pygame
from board import Board
pygame.font.init()

class ColoredSquare:
    def __init__(self, rows, width, color, surface, board):
        self.color = color
        self.x_hover = 0
        self.y_hover = 0
        self.x_click = 0
        self.y_click = 0
        self.rows = rows
        self.width = width / self.rows
        self.surface = surface
        self.board = board

    def draw(self, x_click, y_click):
        self.x_hover, self.y_hover = pygame.mouse.get_pos()

        # Draw blue squares when the mouse is hovered over a number or blank square
        for line in range(self.rows):
            for col in range(self.rows):
                sq_x = col * self.width + 2
                sq_y = line * self.width + 2
                
                if sq_x < self.x_hover < sq_x + self.width and sq_y < self.y_hover < sq_y + self.width:
                    pygame.draw.rect(self.surface, self.color, (sq_x, sq_y, self.width-2, self.width-2))
                
                if sq_x < x_click < sq_x + self.width and sq_y < y_click < sq_y + self.width and self.board[line][col] == 0:
                    pygame.draw.rect(self.surface, self.color, (sq_x, sq_y, self.width-2, self.width-2))


class Button:
    def __init__(self, x, y, width, height, color, text, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('comicsans', 30)
        self.surface = surface

    def draw(self):
        self.label = self.font.render(self.text, 1, self.text_color)
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))
        self.surface.blit(self.label, (self.x + self.width/2 - self.label.get_width()/2, self.y + self.height/2 - self.label.get_height()/2))
    
    def action(self, x_clicked, y_clicked):
        if self.x < x_clicked < self.x + self.width and self.y < y_clicked < self.y + self.height:
            print("Action")

def draw_grid(width, rows, surface, board_nums):
    square_width = width / rows
    quadrant_width = width / (rows//3)
    thickness = 4
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    # Draw vertical lines
    for line in range(rows):
        x1 += square_width
        y1 += square_width

        pygame.draw.line(surface, (0,0,0), (x1,0), (x1, width))
        pygame.draw.line(surface, (0,0,0), (0,y1), (width, y1))
    
    # Draw horizontal lines
    for line in range(rows//3):
        x2 += quadrant_width
        y2 += quadrant_width
        pygame.draw.line(surface, (0,0,0), (x2,0), (x2, width), thickness)
        pygame.draw.line(surface, (0,0,0), (0,x2), (width, x2), thickness)

    # Draw grid numbers
    font = pygame.font.SysFont('comicsans', 30)
    
    for line in range(len(board_nums)):
        for col in range(len(board_nums[line])):
            if board_nums[line][col] != 0:
                text = font.render(f'{board_nums[line][col]}', 1, (0,0,0))
                surface.blit(text, (square_width/2 + col * square_width - text.get_width()/2, square_width/2 + line * square_width - text.get_height()/2))


def draw_window(surface, board, square, width, pos, btn):
    surface.fill((255,255,255))
    square.draw(pos[0], pos[1])
    draw_grid(width, board.rows, surface, board.numbers)
    btn.draw()
    pygame.display.update()


def main():
    # Window settings
    width = 600
    window = pygame.display.set_mode((width+300, width))
    pygame.display.set_caption("Sudoku Game")

    # Variables
    rows = 9
    run = True
    board = Board(rows, rows)
    square = ColoredSquare(rows, width, (0,255,255), window, board.numbers)
    btn = Button(width+100, width/2-25, 100, 50, (255,0,255), "Number", window)
    pos = (0, 0) # Position of the mouse when a button is clicked

    while run:
        draw_window(window, board, square, width, pos, btn)

        # Check if the board is full and if the player won
        # if board.board_full(board.grid):
        #     if board.check_winning():
        #         print("WON!")
        #     else:
        #         print("LOST!")
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                btn.action(pos[0], pos[1])

main()