import pygame, sys
from pygame.locals import *

x = 10
y  = 10
screen = 0

def MyQuit():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global x,y, screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    MyQuit()
                    print("Quit Window")
                elif event.key ==K_LEFT:
                    x = x - 5
                    print("MOVE RECT LEFT")
                elif event.key == K_RIGHT:
                    x = x + 5
                    print("MOVE RECT RIGHT")
                else:
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255), (x, 50,50,10))
    pygame.display.update()

def main():

    global screen 
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 480
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Slither.eat - The Snake Game")

    screen = pygame.display.get_surface()
    pygame.display.set_caption("Snake")
    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()

