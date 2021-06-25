import os
import pygame
from handlers import handle_collide
from config import *
from pygame.time import Clock

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),HWSURFACE|DOUBLEBUF|FULLSCREEN)
# SURFACE = SCREEN.copy()

def draw_window(scale, cards):
    pygame.draw.rect(SCREEN, GREEN_BORDER, BORDER)
    pygame.draw.rect(SCREEN, GREEN_BOARD, BOARD)
    if scale:
        SCREEN.blit(CARDS_IMAGES[0], (cards[0].x, cards[0].y))
        SCREEN.blit(CARDS_IMAGES[0], (cards[1].x, cards[1].y))
        SCREEN.blit(CARDS_IMAGES[0], (cards[2].x, cards[2].y))
    else:
        SCREEN.blit(pygame.transform.scale(CARDS_IMAGES[0], (cards[0].width, cards[0].height)), (cards[0].x, cards[0].y))
        SCREEN.blit(pygame.transform.scale(CARDS_IMAGES[0], (cards[1].width, cards[1].height)), (cards[1].x, cards[1].y))
        SCREEN.blit(pygame.transform.scale(CARDS_IMAGES[0], (cards[2].width, cards[2].height)), (cards[2].x, cards[2].y))
    pygame.display.update()
    SCREEN.blit(pygame.transform.scale(SCREEN, SCREEN.get_rect().size), (0, 0))
    pygame.display.flip()



def main():
    clock = pygame.time.Clock()
    scale = False
    run = True
    TEST_CARD = pygame.Rect((120, 120), (114, 161))
    TEST_CARD2 = pygame.Rect((120, HEIGHT/2-80), (114, 161))
    TEST_CARD3 = pygame.Rect((120, HEIGHT-120-161), (114, 161))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if handle_collide(TEST_CARD):
            scale = True
        else:
            scale = False

        draw_window(scale, [TEST_CARD, TEST_CARD2, TEST_CARD3])

    pygame.quit()

if __name__ == "__main__":
    main()