import pygame, sys
from pygame.locals import *

OSZI = False # outbut is Oszi or Pygame
pygame.init()

BGCOLOR = (100,50,50)
WINDOWHEIGHT = 4000
WINDOWWIDTH = 4000
pos = [WINDOWWIDTH/2,WINDOWHEIGHT/2]

def drawPlayer():
    line(pos[0],pos[1],pos[0]+30,pos[1]+30)




while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()
