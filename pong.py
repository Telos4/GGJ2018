import pygame, sys
from pygame.locals import *
import subprocess

OSZI = False # outbut is Oszi or Pygame
pygame.init()

BGCOLOR = (100,50,50)
pos = [200,200]

def drawPlayer():
    line(pos[0],pos[1],pos[0]+30,pos[1]+30)




while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()
