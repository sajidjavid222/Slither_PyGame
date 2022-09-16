
import pygame, sys
from pygame.locals import *

red = [255,0,0]

#initialize pygame
pygame.init()

#setting up window
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Slither.eat - The Snake Game")

#setting up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
    #main game loop
    for event in pygame.event.get():
        print (event)
        if event.type == QUIT:
            pygame.qiut()
            sys.exit()
    pygame.display.update()