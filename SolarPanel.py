import pygame,sys
from pygame.locals import *
import colour
screen = pygame.display.set_mode((720, 600))
grey=(130,130,124)
darkgrey=(58,58,55)
white=(255,255,255)
screen.fill(white)
pygame.draw.rect(screen,grey,(200,150,300,345))
pygame.draw.rect(screen,darkgrey,(210,160,140,100))
pygame.draw.rect(screen,darkgrey,(210,270,140,100))
pygame.draw.rect(screen,darkgrey,(360,160,130,100))
pygame.draw.rect(screen,darkgrey,(360,270,130,100))
pygame.draw.rect(screen,darkgrey,(210,380,140,100))
pygame.draw.rect(screen,darkgrey,(360,380,130,100))
#pygame.draw.rect(screen,darkgrey,(200,150,300,400))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
