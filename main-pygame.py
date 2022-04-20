import pygame

width = 600
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("Sudoku")

def draw_grid(width, rows, surface):
    line_width1 = width / rows
    line_width2 = width / (rows//3)
    thick = 4
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    for line in range(rows):
        x1 += line_width1
        y1 += line_width1

        pygame.draw.line(surface, (0,0,0), (x1,0), (x1, width))
        pygame.draw.line(surface, (0,0,0), (0,y1), (width, y1))
    
    for line in range(rows//3):
        x2 += line_width2
        y2 += line_width2
        pygame.draw.line(surface, (0,0,0), (x2,0), (x2, width), thick)
        pygame.draw.line(surface, (0,0,0), (0,x2), (width, x2), thick)


def draw_window(surface):
    surface.fill((255,255,255))
    draw_grid(width, 9, surface)
    pygame.display.update()

def main():
    run = True

    while run:
        draw_window(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

main()

