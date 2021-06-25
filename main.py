import os
import pygame
from handlers import handle_collide
from config import *
from pygame.time import Clock

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
SURFACE = SCREEN.copy()

def draw_window(scale, cards):
    pygame.draw.rect(SURFACE, GREEN_BORDER, BORDER)
    pygame.draw.rect(SURFACE, GREEN_BOARD, BOARD)
    if scale:
        SURFACE.blit(CARDS_IMAGES[0], (cards.x, cards.y))
    else:
        SURFACE.blit(pygame.transform.scale(CARDS_IMAGES[0], (cards.width, cards.height)), (cards.x, cards.y))
    pygame.display.update()
    SCREEN.blit(pygame.transform.scale(SURFACE, SCREEN.get_rect().size), (0, 0))
    pygame.display.flip()



def main():
    clock = pygame.time.Clock()
    scale = False
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                x, y = event.size
                x = int(y*1.9)
                SCREEN = pygame.display.set_mode((x,y), HWSURFACE|DOUBLEBUF|RESIZABLE)
        TEST_CARD = pygame.Rect((120, 120), (114, 161))
        if handle_collide(TEST_CARD):
            scale = True
        else:
            scale = False

        draw_window(scale, TEST_CARD)

    pygame.quit()

if __name__ == "__main__":
    main()