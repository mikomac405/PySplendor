import pygame
from config import *

def handle_collide():
    if TEST_CARD.collidepoint(pygame.mouse.get_pos()):
        return True
    return False