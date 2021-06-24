import os
import pygame

FPS = 60
WIDTH, HEIGHT = 1200, 700
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
CARDS_IMAGES = []

for file in os.listdir("cards"):
    img = pygame.image.load(os.path.join("cards",file))
    CARDS_IMAGES.append(img)

TEST_CARD = pygame.Rect(120, 120, 114, 161)

GREEN_BORDER = (0, 155, 80)
GREEN_BOARD = (0, 197, 125)
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
BOARD = pygame.Rect(100, 100, WIDTH-200, HEIGHT-200)