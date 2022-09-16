import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((400,300),0, 32)
pygame.display.set_caption("Drawing")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =  (0, 255, 0)
BLUE = (0,0,255)

window.fill(WHITE)
pygame.draw.polygon(window, GREEN,((146,0),(291,106),(236,300)))