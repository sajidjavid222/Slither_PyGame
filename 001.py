
import pygame
from pygame.locals import *

red = [255,0,0]

#initialize pygame
pygame.init()

#setting up window
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Slither.eat ")

#setting up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
    print("Slither.eat - The Snake Game")
    pass