import os
import pygame
from win32api import GetSystemMetrics
from pygame.locals import *

FPS = 60
HEIGHT= GetSystemMetrics(1)
WIDTH = GetSystemMetrics(0)
CARDS_IMAGES = []

for file in os.listdir("cards"):
    img = pygame.image.load(os.path.join("cards",file))
    CARDS_IMAGES.append(img)



GREEN_BORDER = (0, 155, 80)
GREEN_BOARD = (0, 197, 125)
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
BOARD = pygame.Rect(100, 100, WIDTH-200, HEIGHT-200)