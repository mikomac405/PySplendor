import pygame
from pygame.time import Clock

FPS = 60
WIDTH, HEIGHT = 1200, 700
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PySplendor")

GREEN_BORDER = (0, 155, 80)
GREEN_BOARD = (0, 197, 125)

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
BOARD = pygame.Rect(100, 100, WIDTH-200, HEIGHT-200)

def draw_window():
    pygame.draw.rect(SURFACE, GREEN_BORDER, BORDER)
    pygame.draw.rect(SURFACE, GREEN_BOARD, BOARD)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()