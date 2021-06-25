import pygame
from config import *

def handle_collide(card):
    if card.collidepoint(pygame.mouse.get_pos()):
        return True
    return False