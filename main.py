import os
import pygame
from pygame.time import Clock

FPS = 60
WIDTH, HEIGHT = 1200, 700
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PySplendor")

CARDS_IMAGES = []

for file in os.listdir("Cards"):
    img = pygame.image.load(os.path.join("Cards",file))
    CARDS_IMAGES.append(img)

TEST_CARD = pygame.Rect(120, 120, 114, 161)

GREEN_BORDER = (0, 155, 80)
GREEN_BOARD = (0, 197, 125)
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
BOARD = pygame.Rect(100, 100, WIDTH-200, HEIGHT-200)

def draw_window(scale):
    pygame.draw.rect(SURFACE, GREEN_BORDER, BORDER)
    pygame.draw.rect(SURFACE, GREEN_BOARD, BOARD)
    if scale:
        SURFACE.blit(CARDS_IMAGES[0], (120,120))
    else:
        SURFACE.blit(pygame.transform.scale(CARDS_IMAGES[0], (114,161)), (120,120))
    pygame.display.update()

def handle_collide():
    if TEST_CARD.collidepoint(pygame.mouse.get_pos()):
        return True
    return False

def main():
    clock = pygame.time.Clock()
    scale = False
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if handle_collide():
            scale = True
        else:
            scale = False

        draw_window(scale)

    pygame.quit()

if __name__ == "__main__":
    main()