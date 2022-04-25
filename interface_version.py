import pygame
from board import Board
pygame.font.init()

class ColoredSquare:
    def __init__(self, rows, width, color_hover, color_click, surface, board):
        self.color_hover = color_hover
        self.color_click = color_click
        self.rows = rows
        self.width = width / self.rows
        self.surface = surface
        self.board = board
    
    def draw(self, x_click, y_click):
        x_hover, y_hover = pygame.mouse.get_pos()

        # Draw blue squares when the mouse is hovered over a number or blank square
        for line in range(self.rows):
            for col in range(self.rows):
                sq_x = col * self.width + 2
                sq_y = line * self.width + 2
                
                if sq_x < x_hover < sq_x + self.width and sq_y < y_hover < sq_y + self.width:
                    pygame.draw.rect(self.surface, self.color_hover, (sq_x, sq_y, self.width-2, self.width-2))
                
                if sq_x < x_click < sq_x + self.width and sq_y < y_click < sq_y + self.width and self.board[line][col] == 0:
                    pygame.draw.rect(self.surface, self.color_click, (sq_x, sq_y, self.width-2, self.width-2))
                    self.line = line
                    self.col = col


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
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 0, 15)
        self.surface.blit(self.label, (self.x + self.width/2 - self.label.get_width()/2, self.y + self.height/2 - self.label.get_height()/2))
    
    def clicked(self, x_clicked, y_clicked):
        if self.x < x_clicked < self.x + self.width and self.y < y_clicked < self.y + self.height:
            return True
        return False

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


def draw_window(surface, board, square, width, pos, buttons):
    surface.fill((255,255,255))
    square.draw(pos[0], pos[1])
    draw_grid(width, board.rows, surface, board.numbers)
    
    for btn in buttons:
        btn.draw()
    
    pygame.display.update()


def draw_end_screen(won, surface, width, height):
    font = pygame.font.SysFont('comicsans', 70)
    if won:
        text = font.render("You Won!", 1, (255,0,0))
    else:
        text = font.render("You Lost!", 1, (255,0,0))
    surface.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    pygame.display.update()


def main():
    # Window settings
    grid_width = 600
    screen_width = grid_width+280
    window = pygame.display.set_mode((screen_width, grid_width))
    pygame.display.set_caption("Sudoku Game")

    # Variables
    rows = 9
    run = True
    board = Board(rows, rows)
    square = ColoredSquare(rows, grid_width, (200, 203, 255), (101, 110, 255), window, board.numbers)
    pos = (0, 0) # Position of the mouse when a button is clicked

    buttons = [
        Button(grid_width+50, grid_width/2-90, 50, 50, (255,0,255), "1", window),
        Button(grid_width+115, grid_width/2-90, 50, 50, (255,0,255), "2", window),
        Button(grid_width+180, grid_width/2-90, 50, 50, (255,0,255), "3", window),
        Button(grid_width+50, grid_width/2-25, 50, 50, (255,0,255), "4", window),
        Button(grid_width+115, grid_width/2-25, 50, 50, (255,0,255), "5", window),
        Button(grid_width+180, grid_width/2-25, 50, 50, (255,0,255), "6", window),
        Button(grid_width+50, grid_width/2+40, 50, 50, (255,0,255), "7", window),
        Button(grid_width+115, grid_width/2+40, 50, 50, (255,0,255), "8", window),
        Button(grid_width+180, grid_width/2+40, 50, 50, (255,0,255), "9", window),
    ]
    won = False

    while run:
        draw_window(window, board, square, grid_width, pos, buttons)

        # Check if the board is full and if the player won
        if board.board_full(board.numbers):
            if board.check_winning():
                won = True
            else:
                won = False
            draw_end_screen(won, window, screen_width, grid_width)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                
                for btn in buttons:
                    if btn.clicked(pos[0], pos[1]):
                        board.numbers[square.line][square.col] = int(btn.text)
        
        if not run:
            pygame.time.wait(3000)

main()