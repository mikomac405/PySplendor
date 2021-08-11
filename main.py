import os
import pygame
from handlers import handle_collide
from config import *
from pygame.time import Clock


def draw_window(scale):
    pygame.draw.rect(SURFACE, GREEN_BORDER, BORDER)
    pygame.draw.rect(SURFACE, GREEN_BOARD, BOARD)
    if scale:
        SURFACE.blit(CARDS_IMAGES[0], (120,120))
    else:
        SURFACE.blit(pygame.transform.scale(CARDS_IMAGES[0], (114,161)), (120,120))
    pygame.display.update()



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

